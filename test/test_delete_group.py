#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample script to delete a role.
"""

from __future__ import print_function

from appd.cmdline import parse_argv
from appd.request import AppDynamicsClient

import random
import string
import time
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
    response = c.create_group(group_name, 'description to test group')
    print(response)
    response = c.delete_group(response['id'])
    print(response)
else:
    print('Application, not found!')


