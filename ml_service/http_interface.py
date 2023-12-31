#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:45:33 2023

@author: zby
"""
import sys
sys.path.append('..')
import pickle
from flask import Flask, request, jsonify, render_template
from utils.db import DB
from feature_engineering import feature_extract, dump_feats_into_mysql


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
db = DB('spec2017')


def dump_api_info_into_mysql(form):
    db.execute("""replace into cpu_api_info (benchmark,sys,cores,chips
               ,enabled_threads_per_core,processor_mhz,parallel,base_pointer_size
               ,peak_pointer_size,first_level_cache,second_level_cache
               ,third_level_cache,other_cache,memory,storage)
               values ('{}','{}','{}','{}','{}','{}','{}','{}'
                       ,'{}','{}','{}','{}','{}','{}','{}')"""
               .format(form['benchmark'], form['sys'], form['cores'], form['chips']
                       , form['enabled_threads_per_core'], form['processor_mhz']
                       , form['parallel'], form['base_pointer_size']
                       , form['peak_pointer_size']
                       , form['first_level_cache'], form['second_level_cache']
                       , form['third_level_cache'], form['other_cache'], form['memory']
                       , form['storage']))
    # 特征处理
    raw_data = db.select_df("""select * from cpu_api_info 
                            order by update_time desc
                            limit 1""")
    features = feature_extract(raw_data)
    dump_feats_into_mysql(features)
    
    
def predict_use_api(form, label='base_result'):
    model = pickle.load(
            open("./model_save/model_{}_{}.pkl".format(form['benchmark'], label), "rb"))
    data = db.select_df("""select * from ml_cpu2017_feature 
                     where sys = '{}' and benchmark = '{}'
                     and base_result = -1 and peak_result = -1
                     order by update_time desc
                     limit 1"""
                     .format(form['sys'], form['benchmark']))
    X = data.loc[:, ~data.columns.isin(['benchmark', 'sys', 'update_time'] \
                                      + ['base_result', 'peak_result'])].values
    result = model.predict(X)
    return '您所提供的硬件参数的{} '.format(form['benchmark']) + label + \
        ' 的预测值为: ' + str(round(result[0], 1))


@app.route('/')
def hello():
    return render_template('./index.html')


@app.route('/cpu', methods=['POST'])
def register_cpu():
    form = request.form
    dump_api_info_into_mysql(form)
    result = predict_use_api(form)
    return result


if __name__ == '__main__':
    app.run(host='172.30.169.113', port=5000, debug=False)
