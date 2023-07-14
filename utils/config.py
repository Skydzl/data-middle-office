#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:48:35 2023

@author: zby
"""

""" 配置文件读取 """

import configparser
import copy
import os
from collections import namedtuple

_current_dir = os.path.dirname(os.path.abspath(__file__))
_config = configparser.ConfigParser()
_config.read(_current_dir + '/../resources/config.ini')
_DBConfig = namedtuple('DBConfig', ['host', 'port', 'user', 'pwd', 'db'])


def get(key):
    return copy.deepcopy(_config[key])


def db_config(scheme):
    key = 'db-' + scheme
    if key in _config:
        dbc = _config[key]
        return _DBConfig(dbc['host'], int(dbc['port']), dbc['user'],
                         dbc['pwd'], dbc['db'])
    else:
        raise AttributeError('No Such DB Scheme')
