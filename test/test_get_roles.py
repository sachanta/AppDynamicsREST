#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample script to print a list of roles from the specified controller and app.
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
    allRoles = c.get_roles()
    print('All Roles -- %s', allRoles)
    print(allRoles[0].name)
    firstRole_uisng_by_name = allRoles.by_name(allRoles[0].name)
    print('First Role using name -- %s', firstRole_uisng_by_name)
    secondRole_using_by_id = allRoles.by_id(allRoles[1].id)
    print('Second Role using id -- %s', secondRole_using_by_id)
    thirdRole_using_get_Role = c.get_role(allRoles[1].id)
    print('Third Role using get_Role -- %s', thirdRole_using_get_Role)
else:
    print('Application, not found!')
