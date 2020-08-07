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
    print('All Users -- %s', allUsers)
    print(allUsers[0].name)
    firstUser_uisng_by_name = allUsers.by_name(allUsers[0].name)
    print('First User using name -- %s', firstUser_uisng_by_name)
    secondUser_using_by_id = allUsers.by_id(allUsers[1].id)
    print('Second User using id -- %s', secondUser_using_by_id)
    thirdUser_using_get_User = c.get_user(allUsers[1].id)
    print('Third User using get_User -- %s', thirdUser_using_get_User)

else:
    print('Application, not found!')
