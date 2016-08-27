#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""Building paths with the operator
"""
#end_pymotw_header

import pathlib

usr = pathlib.PurePosixPath('/usr')
print(usr)

usr_local = usr / 'local'
print(usr_local)

root = usr / '..'
print(root)

etc = root / '/etc/'
print(etc)
