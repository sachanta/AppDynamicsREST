#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample script to add a user to a group.
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
    group_name = get_random_string(5)
    group = c.create_group(group_name, 'description to test group')
    first_name = get_random_string(5)
    second_name = get_random_string(5)
    email = first_name + '.' + second_name + '@email.com'
    user = c.create_user_v1(first_name, first_name, email, 'password', 'INTERNAL')
    print(group['id'], group['name'], user['id'], user['name'])
    response = c.add_user_to_group(group['id'], user['id'])

    # clean up
    c.remove_user_from_group(group['id'], user['id'])
    c.delete_user(user['id'])
    c.delete_group(group['id'])

    print(response)
else:
    print('Application, not found!')
