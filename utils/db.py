#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:48:35 2023

@author: zby
"""

""" 数据库操作封装 """

import logging
import traceback
from collections import namedtuple
import pymysql.cursors
import sys

from utils.config import *
import pandas as pd
logger = logging.getLogger("DB")


class DB:

    def __init__(self, scheme='tv_show'):
        self._config = db_config(scheme)
        self._host = self._config.host
        self._port = self._config.port
        self._user = self._config.user
        self._pwd = self._config.pwd
        self._db = self._config.db

    def __repr__(self):
        return self._config

    def _connect(self):
        return pymysql.connect(host=self._host,
                               user=self._user,
                               passwd=self._pwd,
                               db=self._db,
                               port=self._port,
                               charset="utf8",
                               cursorclass=pymysql.cursors.DictCursor)

    def select(self, sql, args=None):
        conn = self._connect()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, args)
            return cursor.fetchall()
        except:
            logger.error("select error, sql is %s, args is %s", sql, args)
            traceback.print_exc(file=sys.stdout)
        finally:
            cursor.close()
            conn.close()
        return None

    def single(self, sql, args=None):
        conn = self._connect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, args)
                return cursor.fetchone()
        except:
            logger.error("single error, sql is %s, args is %s", sql, args)
            traceback.print_exc(file=sys.stdout)
        finally:
            conn.close()
        return None

    def insert(self, obj: namedtuple):
        return self.batch_insert([obj])

    def select_df(self, sql: object, args: object = None) -> object:
        conn = self._connect()
        cursor = conn.cursor()
        try:
            return pd.read_sql(sql=sql, con=conn)
        except:
            logger.error("select error, sql is %s, args is %s", sql, args)
            traceback.print_exc(file=sys.stdout)
        finally:
            cursor.close()
            conn.close()
        return None

    def batch_insert(self, objs):
        if len(objs) == 0:
            return 0
        fields = objs[0]._fields
        placeholders = tuple('%s' for f in fields)
        datas = [tuple(o) for o in objs]
        table = objs[0].__class__.__name__
        sql = "insert into %s %s values %s" % (table, fields, placeholders)
        sql = sql.replace('\'', '')
        return self.batch_execute(sql, datas)

    def batch_replace(self, objs):
        if len(objs) == 0:
            return 0
        fields = objs[0]._fields
        placeholders = tuple('%s' for f in fields)
        datas = [tuple(o) for o in objs]
        table = objs[0].__class__.__name__
        sql = "replace into %s %s values %s" % (table, fields, placeholders)
        sql = sql.replace('\'', '')
        return self.batch_execute(sql, datas)

    def update(self, obj: namedtuple):
        return self.batch_update([obj])

    def update(self, obj: namedtuple):
        return self.batch_update([obj])

    def batch_update(self, objs):
        if len(objs) == 0:
            return 0
        fields = objs[0]._fields
        placeholders = ', '.join(tuple(f + ' = %s' for f in fields if f != 'id'))
        table = objs[0].__class__.__name__
        datas = []
        for obj in objs:
            data = [getattr(obj, f) for f in fields]
            datas.append(tuple(data[1:] + data[:1]))
        sql = "update %s set %s where id = " % (table, placeholders)
        sql = sql.replace('\'', '') + '%s'
        print(sql)
        return self.batch_execute(sql, datas)

    def execute(self, sql, args=None):
        conn = self._connect()
        cursor = conn.cursor()
        try:
            count = cursor.execute(sql, args)
            conn.commit()
        except:
            logger.error("execute error. sql is %s, args is %s", sql, args)
            traceback.print_exc(file=sys.stdout)
            count = 0
        finally:
            conn.close()
        return count

    def batch_execute(self, sql, args=None):
        conn = self._connect()
        cursor = conn.cursor()
        try:
            count = cursor.executemany(sql, args)
            conn.commit()
        except:
            count = 0
            logger.error("batch execute error. sql is %s, args is %s", sql, args)
            traceback.print_exc(file=sys.stdout)
        finally:
            conn.close()
        return count


if __name__ == '__main__':
    db = DB('tv_show')
    print(db.select("select * from tvshow_raw_features limit 10"))
