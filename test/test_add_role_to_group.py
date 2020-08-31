#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample script to add role to group.
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
    group_name = get_random_string(5)
    group = c.create_group(group_name, 'description to test group')
    response = c.add_role_to_group(role['id'], group['id'])
    print(role['id'], role['name'], group['id'], group['name'])

    # clean up
    c.remove_role_from_group(role['id'], group['id'])
    c.delete_role(role['id'])
    c.delete_group(group['id'])
    print(response)
else:
    print('Application, not found!')
