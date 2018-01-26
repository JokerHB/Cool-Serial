#! /usr/bin/env python
# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

base = 'Win32GUI'
# base = 'Console'
# base = 'ConsoleKeepPath'
# base = 'Win32GUI'
# base = 'Win32Service'

executables = [
    Executable('main.py', base = base)
]

setup(name = 'main app',
      version = '1.0',
      description = 'main app',
      executables = executables
      )