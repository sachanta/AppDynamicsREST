#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sample script to print a list of events from the specified controller and app.
"""

from __future__ import print_function

from appd.cmdline import parse_argv
from appd.request import AppDynamicsClient

__author__ = 'Kyle Furlong'
__copyright__ = 'Copyright (c) 2013-2017 AppDynamics Inc.'


args = parse_argv()
c = AppDynamicsClient(args.url, args.username, args.password, args.account, args.verbose)

apps = c.get_applications()
if len(apps) > 0:
    resp = c.create_event(apps[0].id,
                          summary='Event 1',
                          comment='This is an event created by the Python SDK',
                          severity='INFO',
                          eventtype='APPLICATION_CONFIG_CHANGE')
    print(resp)
    resp = c.create_event(app_id=10,
                          summary='Custom Event 1',
                          comment='This is an event created by the Python SDK',
                          severity='INFO',
                          eventtype='CUSTOM',
                          customeventtype='MYCUSTOMEVENT',
                          node="Node_8000",
                          tier="ECommerce Server",
                          bt="ViewItems.getAllItems")
    print(resp)


else:
    print('no applications found!')
