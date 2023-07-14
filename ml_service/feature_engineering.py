#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 17:08:32 2023

@author: zby
"""
import sys
sys.path.append("..")

import re
import warnings
import pandas as pd
from utils.db import DB
from utils.log import Log


warnings.filterwarnings('ignore')
db = DB('spec2017')
logger = Log('feature')

'''
    对于cpu2017的每个benchmark分别建立xgb的模型。拟作特征如下：
        cores 核心数 fromDB
        chips 芯片数 fromDB
        enabled_threads_per_core 单核线程数 fromDB
        processor_mhz 处理器赫兹 fromDB
        parallel 是否并行 需做处理
        base_pointer_size 基础指针大小 需做处理
        peak_pointer_size 最大指针大小 需做处理
        first_level_cache 第一cache大小 需做处理
        second_level_cache 第二cache大小 需做处理
        third_level_cache 第三cache大小 需做处理
        other_cache 其他cache大小 需做处理
        memory 内存大小 需做处理
        storage 存储大小 需做处理
        -- operating_system 看初模型结果是否需要加入该特征
        -- file_system 看初模型结果是否需要加入该特征
        -- compiler 看初模型结果是否需要加入该特征
'''


def feats_pointer(x):
    """
    指针类特征处理
    """
    if x == '64-bit':
        return 64
    elif x == '32-bit':
        return 32
    elif x == '32/64-bit':
        return 48
    elif x == 'Not Applicable':
        return 0
    else:
        raise ValueError('指针大小的值格式不对，该大小为:{}'.format(x))
        
        
def feats_1stcache(x):
    """
    指针类特征处理
    """
    if x == '16 KB I + 16 KB D on chip per core':
        return 1
    elif x == '32 KB I + 32 KB D on chip per core':
        return 2
    elif x == '32 KB I + 48 KB D on chip per core':
        return 3
    elif x == '32 KB I + 64 KB D on chip per core':
        return 4
    elif x == '64 KB I + 32 KB D on chip per core':
        return 5
    elif x == '64 KB I + 64 KB D on chip per core':
        return 6
    elif x == '96 KB I + 64 KB D on chip per core':
        return 7
    elif x == 'redacted':
        return 0
    else:
        raise ValueError('1stcache的值格式不对，为:{}'.format(x))
        
        
def feats_2ndcache(x):
    if x == '256 KB I+D on chip per core':
        return 1
    elif x == '512 KB I+D on chip per core':
        return 2
    elif x == '1 MB I+D on chip per core':
        return 4
    elif x == '1.25 MB I+D on chip per core':
        return 5
    elif x in ('2 MB I+D on chip per core', '2 MB I+D on chip per chip'):
        return 8
    elif x == '2 MB I on chip per chip (256 KB / 4 cores); 4 MB D on chip per chip (256 KB / 2 cores)':
        return 6
    elif x == 'redacted':
        return 0
    else:
        raise ValueError('2ndcache的值格式不对，为:{}'.format(x))
    

def feats_3rdcache(x):
    if x == 'redacted':
        return 0
    keylist = re.findall('[0-9]*\.*[0-9]+ [MGT]B ', x)
    if keylist == []:
        raise ValueError('3rdcache的值格式不对，为:{}'.format(x))

    value, unit = keylist[0].split(' ')[:2]

    if unit == 'KB':
        base = 1024  
    elif unit == 'MB':
        base = 1
    elif unit == 'GB':
        base = 1 / 1024
    else:
        raise ValueError('3rdcache的值格式不对，为:{}'.format(x))
    return float(value) / base


def feats_othercache(x):
    if x == '16 MB I+D off chip per 8 DIMMs':
        return 8
    elif x == '16 MB I+D off chip per 2 DIMMs':
        return 2
    elif x == 'None':
        return 0
    else:
        raise ValueError('othercache的值格式不对，为:{}'.format(x))
        
    
def feats_memory(x):
    keylist = re.findall('[0-9]+\.{0,1}[0-9]+ [MGT]B', x)
    if keylist == []:
        raise ValueError('memory的值格式不对，为:{}'.format(x))
    value, unit = keylist[0].split(' ')[:2]

    if unit == 'TB':
        base = 1024
    elif unit == 'GB':
        base = 1
    elif unit == 'MB':
        base = 1 / 1024
    else:
        raise ValueError('memory的值格式不对，为:{}'.format(x))
    return float(value) * base


def feats_storage(x):
    # 提取单位和值，分两次提取
    keylist = re.findall('[0-9]+ *x *[0-9]+\.*[0-9]* *[MGT]B', x)
    if keylist != []: # 有乘法的
        value, unit = keylist[0][:-2], keylist[0][-2:]    
        value1, value2 = value.split('x')
        value1, value2 = float(value1.replace(' ', '')), float(
            value2.replace(' ', ''))
        value = value1 * value2
        
    else: # 没乘法的
        keylist = re.findall('[0-9]+\.*[0-9]* *[MGT]B{0,1}', x)
        if keylist[0][-1] == 'B':
            value, unit = keylist[0][:-2], keylist[0][-2:]  
        else:
            value, unit = keylist[0][:-1], keylist[0][-1:] + 'B'
        
        value = float(value)
    
    # 单位划分    
    if unit == 'TB':
        base = 1024
    elif unit == 'GB':
        base = 1
    elif unit == 'MB':
        base == 1 / 1024        

    return value * base
    

def feature_extract(raw_data):
    features = pd.DataFrame(data=None, columns=['benchmark','sys','cores'
                                ,'chips','enabled_threads_per_core','processor_mhz'
                                ,'parallel','base_pointer_size','peak_pointer_size'
                                ,'first_level_cache','second_level_cache'
                                ,'third_level_cache','other_cache','memory'
                                ,'storage','base_result','peak_result'])
    # meta信息
    features['benchmark'] = raw_data['benchmark']
    features['sys'] = raw_data['sys']
    
    # 直接从数据库拿到的
    features['cores'] = raw_data['cores']
    features['chips'] = raw_data['chips']
    features['enabled_threads_per_core'] = raw_data['enabled_threads_per_core']
    features['processor_mhz'] = raw_data['processor_mhz']
    
    if 'update_time' not in raw_data.columns:
        features['base_result'] = raw_data['base_result']
        features['peak_result'] = raw_data['peak_result']
    else:
        features['base_result'] = -1
        features['peak_result'] = -1

    # 需做处理的特征
    features['parallel'] = raw_data['parallel'].apply(lambda x: 1 if x == 'Yes' else 0)
    features['base_pointer_size'] = raw_data['base_pointer_size'].apply(
        lambda x: feats_pointer(x))
    features['peak_pointer_size'] = raw_data['peak_pointer_size'].apply(
        lambda x: feats_pointer(x))
    features['first_level_cache'] = raw_data['first_level_cache'].apply(
        lambda x: feats_1stcache(x))
    features['second_level_cache'] = raw_data['second_level_cache'].apply(
        lambda x: feats_2ndcache(x))
    features['third_level_cache'] = raw_data['third_level_cache'].apply(
        lambda x: feats_3rdcache(x))
    features['other_cache'] = raw_data['other_cache'].apply(
        lambda x: feats_othercache(x)) 
    features['memory'] = raw_data['memory'].apply(
        lambda x: feats_memory(x)) 
    features['storage'] = raw_data['storage'].apply(
        lambda x: feats_storage(x)) 
    return features


def dump_feats_into_mysql(features):
    for index, row in features.iterrows():
        logger.info("{}\t{}".format(row['benchmark'], row['sys']))
        db.execute("""replace into ml_cpu2017_feature 
                   (benchmark,sys,cores,chips,enabled_threads_per_core
                    ,processor_mhz,parallel,base_pointer_size,peak_pointer_size
                    ,first_level_cache,second_level_cache,third_level_cache
                    ,other_cache,memory,storage,base_result,peak_result)
                   values ('{}','{}','{}','{}','{}','{}','{}','{}'
                           ,'{}','{}','{}','{}','{}','{}','{}','{}','{}') """
                   .format(row['benchmark'],row['sys'],row['cores'],row['chips']
                           ,row['enabled_threads_per_core'],row['processor_mhz']
                           ,row['parallel'],row['base_pointer_size']
                           ,row['peak_pointer_size'],row['first_level_cache']
                           ,row['second_level_cache'],row['third_level_cache']
                           ,row['other_cache'],row['memory'],row['storage']
                           ,row['base_result'],row['peak_result']))
        

class feature_cpu2017:
    """特征提取"""
    def __init__(self):
        self.raw_data = db.select_df("select * from cpu2017")
        self.features = feature_extract(self.raw_data)
        dump_feats_into_mysql(self.features)
    

if __name__ == "__main__":
    extractor = feature_cpu2017()




