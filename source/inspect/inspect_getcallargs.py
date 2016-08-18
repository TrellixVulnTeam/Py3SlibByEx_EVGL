#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Show how values map to function arguments.
"""
#end_pymotw_header

import inspect
import example
import pprint

INPUTS = [
    (('a',), {'unknown_name': 'value'}),
    (('a',), {'arg2': 'value'}),
    (('a', 'b', 'c', 'd'), {}),
    ((), {'arg1': 'a'}),
]

for args, kwds in INPUTS:
    print(args, kwds)
    callargs = inspect.getcallargs(example.module_level_function,
                                   *args, **kwds)
    pprint.pprint(callargs, width=74)
    example.module_level_function(**callargs)
    print()
