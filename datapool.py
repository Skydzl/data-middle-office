#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:48:35 2023

@author: zby
"""

"""
    数据中台第一层，汇聚整合
    把处理好的干净数据录入数据库
"""

import pandas as pd

from utils.db import DB
from utils.log import Log
import utils.df as dfu
from unify_field import unify_field_name
from data_clean_func import clean_fill_nan_with_empty, clean_datetime_unify


db = DB('spec2017')
logger = Log('datapool')


class CloseRawDataLayer:
    """
    贴源数据层
    实现功能：
        1. 数据采集（静态方式或动态方式）
        2. 数据清洗
        3. 数据存储（将清洗后的数据存入mysql）
    """
    def __init__(self, flow_process: bool):
        self._flow_process = flow_process
        cleaned_datas = self._clean(self.load_raw_data())
        self.dump_raw_into_db(cleaned_datas)

    def load_raw_data(self):
        """
        读取原始数据
        :return DataFrame obj:  
        """
        if self._flow_process:
            # 动态获取数据，爬虫
            pass
        else:
            # 静态获取数据
            cpu2017_data = pd.read_csv(r'raw/cpu2017-results-20230413-222853.csv')
            cpu2006_data = pd.read_csv(r'raw/cpu2006-results-20230523-015835.csv')
            java2015_data = pd.read_csv(r'raw/jbb2015-results-20230518-023254.csv')
            java2008_data = pd.read_csv(r'raw/jvm2008-results-20230523-015714.csv')
            power_data = pd.read_csv(r'raw/power_ssj2008-results-20230518-025251.csv', encoding='gbk')
        return cpu2017_data, cpu2006_data, java2015_data, java2008_data, power_data

    def _clean(self, raw_datas):
        """
        清洗原始数据
        1.字段对齐
        2.填充空值
        """
        cpu2017_data, cpu2006_data, java2015_data, java2008_data, power_data = raw_datas
        
        cpu2017_data = unify_field_name(cpu2017_data, tablename='cpu2017')
        cpu2017_data = clean_fill_nan_with_empty(cpu2017_data)
        clean_datetime_unify(cpu2017_data, datetime_fields=['hw_avail', 'sw_avail', 'test_date', 'published', 'updated'])
        
        java2015_data = unify_field_name(java2015_data, tablename='jbb2015')
        java2015_data = clean_fill_nan_with_empty(java2015_data)
        clean_datetime_unify(java2015_data, datetime_fields=['hw_avail', 'os_avail', 'jvm_avail', 'sw_avail', 'published', 'updated'])
        
        power_data = unify_field_name(power_data, tablename='power_ssj2008')
        power_data = clean_fill_nan_with_empty(power_data)
        clean_datetime_unify(power_data, datetime_fields=['hw_avail', 'sw_avail', 'test_date', 'published', 'updated'])
        
        cpu2006_data = unify_field_name(cpu2006_data, tablename='cpu2006')
        cpu2006_data = clean_fill_nan_with_empty(cpu2006_data)
        clean_datetime_unify(cpu2006_data, datetime_fields=['hw_avail', 'sw_avail', 'test_date', 'published', 'updated'])
        
        java2008_data = unify_field_name(java2008_data, tablename='jvm2008')
        java2008_data = clean_fill_nan_with_empty(java2008_data)
        clean_datetime_unify(java2008_data, datetime_fields=['hw_avail', 'os_avail', 'sw_avail', 'test_date', 'published', 'updated'])
        
        return cpu2017_data, cpu2006_data, java2015_data, java2008_data, power_data

    def dump_raw_into_db(self, cleaned_datas):
        cpu2017_clean_data, cpu2006_clean_data, java2015_clean_data\
            , java2008_clean_data, power_clean_data = cleaned_datas
        
        test_tuples = dfu.df2str_namedtuple('cpu2017', cpu2017_clean_data)
        db.batch_replace(test_tuples)
        logger.info('{}数据已存入数据库'.format('cpu2017'))
        
        test_tuples = dfu.df2str_namedtuple('jbb2015', java2015_clean_data)
        db.batch_replace(test_tuples)
        logger.info('{}数据已存入数据库'.format('jbb2015'))
        
        test_tuples = dfu.df2str_namedtuple('jvm2008', java2008_clean_data)
        db.batch_replace(test_tuples)
        logger.info('{}数据已存入数据库'.format('jvm2008'))

        test_tuples = dfu.df2str_namedtuple('power_ssj2008', power_clean_data)
        db.batch_replace(test_tuples)
        logger.info('{}数据已存入数据库'.format('power_ssj2008'))
        
        test_tuples = dfu.df2str_namedtuple('cpu2006', cpu2006_clean_data)
        db.batch_replace(test_tuples)
        logger.info('{}数据已存入数据库'.format('cpu2006'))


if __name__ == "__main__":
    close_raw_data_layer = CloseRawDataLayer(flow_process=False)