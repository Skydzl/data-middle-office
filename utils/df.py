#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:48:35 2023

@author: zby
"""

"""
    pandas DataFrame 工具
"""
from collections import namedtuple


def df2namedtuple(name, df):
    columns = df.columns.tolist()
    def_tuple = namedtuple(name, columns)
    tuples = []
    for index, row in df.iterrows():
        tuples.append(def_tuple(**row))
    return tuples


def df2str_namedtuple(name, df):
    columns = df.columns.tolist()
    def_tuple = namedtuple(name, columns)
    tuples = []
    for index, row in df.iterrows():
        tmp = dict(row)
        for k, v in tmp.items():
            if isinstance(v, list) or isinstance(v, dict) or isinstance(v, tuple):
                tmp[k] = str(v)
        tuples.append(def_tuple(**tmp))
    return tuples
