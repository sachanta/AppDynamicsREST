#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample script to print a list of groups from the specified controller and app.
"""

from __future__ import print_function
from appd.cmdline import parse_argv
from appd.request import AppDynamicsClient

__author__ = 'Srikar Achanta'
__copyright__ = 'Copyright (c) 2013-2020 AppDynamics Inc.'


args = parse_argv()
c = AppDynamicsClient(args.url, args.username, args.password, args.account, args.verbose)

apps = c.get_applications()
if len(apps) > 0:
    allUsers = c.get_users()
    print('All Users -- \n%s' % allUsers)
    print('User using get_user_by_id -- \n%s' % c.get_user_by_id(allUsers[1].id))
    print('User using get_user_by_name -- \n%s' % c.get_user_by_name(allUsers[1].name))

else:
    print('Application, not found!')
