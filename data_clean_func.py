#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 21:59:15 2023

@author: zby
"""
from datetime import datetime


def clean_fill_nan_with_empty(raw_data):
    """
    :param raw_data: DataFrame obj 待处理数据
    :return: 将所有的nan值填充为空字符
    """
    return raw_data.fillna('')


def clean_datetime_unify(raw_data, datetime_fields):
    for field in datetime_fields:
        raw_data.loc[:, field] = raw_data[field].apply(datetime2str)


def datetime2str(dt):
    if dt == '':
        return ''
    if len(dt) == 5:
        dt = '0' + dt
    try:
        dt_fmt = datetime.strptime(dt, '%b-%y') # 6位
    except ValueError:
        try:
            dt_fmt = datetime.strptime(dt, '%Y-%m') # 7位
        except ValueError:
            try:
                dt_fmt = datetime.strptime(dt, '%b-%Y') # 8位
            except ValueError:   
                try:
                    dt_fmt = datetime.strptime(dt, '%y-%b') # 6位
                except ValueError:
                    print(dt)
        
    return datetime.strftime(dt_fmt, '%Y-%m-%d')