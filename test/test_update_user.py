#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample script to update a user for the specified controller.
"""

from __future__ import print_function

from appd.cmdline import parse_argv
from appd.request import AppDynamicsClient

import random
import string
import requests

__author__ = 'Srikar Achanta'
__copyright__ = 'Copyright (c) 2013-2020 AppDynamics Inc.'

args = parse_argv()
c = AppDynamicsClient(args.url, args.username, args.password, args.account, args.verbose)

apps = c.get_applications()


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


if len(apps) > 0:
    user_name = get_random_string(5)
    email = user_name + '@' + 'gmail.com'
    response = c.create_user_v1(user_name, user_name, email, 'password', 'INTERNAL')
    print(response)
    resp = c.update_user(response['id'], get_random_string(5), "new-display-name")
    print(resp)
    c.delete_user(response['id'])
else:
    print('Application, not found!')
