#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample script to print a list of events from the specified controller and app.
"""

from __future__ import print_function

from appd.cmdline import parse_argv
from appd.request import AppDynamicsClient

import random
import string

__author__ = 'Kyle Furlong'
__copyright__ = 'Copyright (c) 2013-2017 AppDynamics Inc.'

args = parse_argv()
c = AppDynamicsClient(args.url, args.username, args.password, args.account, args.verbose)

apps = c.get_applications()


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


if len(apps) > 0:

    first_name = get_random_string(5)
    second_name = get_random_string(5)
    email = first_name + '.' + second_name + '@email.com'

    resp = c.create_user(first_name, second_name, email,
                         user_password='johndoe', user_roles='Administrator,Universal Agent User')
    print(resp)
else:
    print('Application, not found!')


