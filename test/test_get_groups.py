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
    print('All Groups -- \n%s' % allGroups)
    print('Group using get_group_by_id -- \n%s' % c.get_group_by_id(allGroups[1].id))
    print('Group using get_group_by_name -- \n%s' % c.get_group_by_name(allGroups[1].name))
else:
    print('Application, not found!')
