#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample script to remove a role from user.
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
    role_name = get_random_string(5)
    role = c.create_role(role_name, 'description to test role')
    first_name = get_random_string(5)
    second_name = get_random_string(5)
    email = first_name + '.' + second_name + '@email.com'
    user = c.create_user_v1(first_name, first_name, email, 'password', 'INTERNAL')
    print(role['id'], role['name'], user['id'], user['name'])
    c.add_role_to_user(role['id'], user['id'])
    response = c.remove_role_from_user(role['id'], user['id'])
    print(response)
    # clean up
    c.delete_user(user['id'])
    c.delete_role(role['id'])
else:
    print('Application, not found!')
