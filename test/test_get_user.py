#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample script to print a user.
"""

from __future__ import print_function

from appd.cmdline import parse_argv
from appd.request import AppDynamicsClient

__author__ = 'Srikar Achanta'
__copyright__ = 'Copyright (c) 2013-2020 AppDynamics Inc.'


args = parse_argv()
c = AppDynamicsClient(args.url, args.username, args.password, args.account, args.verbose)

resp = c.get_user(user_id=15)
print(resp)

resp1 = c.get_users()
print(resp1)
