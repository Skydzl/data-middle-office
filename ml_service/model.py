#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:44:32 2023

@author: zby
"""
import sys
sys.path.append('..')
import pickle
# import numpy as np
import xgboost as xgb
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn import metrics

from utils.db import DB
from utils.log import Log
# import utils.number as number


db = DB('spec2017')
logger = Log('model')
labels = ['base_result', 'peak_result']


class TrainModel:
    
    def __init__(self, benchmark, label):
        data = db.select_df("""select * from ml_cpu2017_feature
                            where benchmark = '{}'
                            and base_result != -1
                            and peak_result != -1""".format(benchmark))
        self.benchmark = benchmark
        self.label = label
        self.X = data.loc[:, ~data.columns.isin(['benchmark', 'sys', 'update_time'] \
                                          + labels)].values
        self.y = data.loc[:, label].values
        self.train_x, self.test_x, self.train_y, self.test_y = train_test_split(
            self.X, self.y)
        
    def train(self):
        logger.info("寻找最优参数 wait....")
        
        xgb_param_grid = {'learning_rate': [i / 10 for i in range(0, 2)],
                          'max_depth': [i for i in range(1, 10)],
                          'n_estimators': [i for i in range(50, 400, 20)]}
        mae = metrics.make_scorer(metrics.mean_absolute_error, greater_is_better=False)
        # self.model = GridSearchCV(xgb.XGBRegressor(), cv=5, param_grid=xgb_param_grid, scoring=mae)
        # best_params = self.model.fit(self.train_x, self.train_y).best_params_
        
        best_params = {'learning_rate': 0.1, 'max_depth': 9, 'n_estimators': 210} # CINT2017 
        # best_params = {'learning_rate': 0.1, 'max_depth': 9, 'n_estimators': 290} # CFP2017rate
        # best_params = {'learning_rate': 0.1, 'max_depth': 7, 'n_estimators': 390} # CINT2017rate
        # best_params = {'learning_rate': 0.1, 'max_depth': 9, 'n_estimators': 310} # CFP2017
        print(best_params)
        self.model = xgb.XGBRegressor(max_depth=best_params['max_depth'],
                                      learning_rate=best_params['learning_rate'],
                                      n_estimators=best_params['n_estimators'])
        
        self.model.fit(self.train_x, self.train_y)
        pickle.dump(self.model,
                    open(
                        "./model_save/model_{}_{}.pkl".format(self.benchmark, self.label),
                        "wb"))
        
        # -------------- 训练集误差 --------------
        self.train_pred_y = self.model.predict(self.train_x)
        train_mape = metrics.mean_absolute_error(self.train_y, self.train_pred_y)
        logger.info("训练集MAE：%s", train_mape)
        
    def evaluate(self):
        self.test_pred_y = self.model.predict(self.test_x)
        test_mape = metrics.mean_absolute_error(self.test_y, self.test_pred_y)
        logger.info("测试集MAE：%s", test_mape)
        
        
if __name__ == "__main__":
    train_model = TrainModel(benchmark='CINT2017', label='base_result')
    train_model.train()
    train_model.evaluate()
        
        
        
        
        
        
        