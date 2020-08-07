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
    allGroups = c.get_groups()
    print('All Groups -- %s', allGroups)
    print(allGroups[0].name)
    firstGroup_uisng_by_name = allGroups.by_name(allGroups[0].name)
    print('First Group using name -- %s', firstGroup_uisng_by_name)
    secondGroup_using_by_id = allGroups.by_id(allGroups[1].id)
    print('Second Group using id -- %s', secondGroup_using_by_id)
    thirdGroup_using_get_group = c.get_group(allGroups[1].id)
    print('Third Group using get_group -- %s', thirdGroup_using_get_group)
else:
    print('Application, not found!')
