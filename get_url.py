#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 12:10:18 2023

@author: zby
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup
from utils.db import DB
import utils.df as dfu


db = DB('spec2017')
base_url = "https://spec.org/cpu2017/results/"


def dump_urls_into_mysql(quarter_res_urls, tablename, update=False):
    """
    :param update: update=True 则仅更新增量，update=False 则更新全量
    """
    url_tables = []
    if update:
        quarter_res_urls = quarter_res_urls[:-1]
        
    for q_url in quarter_res_urls:
        url_table = pd.DataFrame(data=None, columns=['tablename', 'url'])
        bs = BeautifulSoup(requests.get(q_url).text, 'html.parser')
        disclosures = bs.find_all(attrs={'class': 'disclosures'})
        disclosures = [q_url + '/'+ d.a['href'] for d in disclosures]
        url_table['url'] = disclosures
        url_table['tablename'] = tablename
        url_tables.append(url_table)
    
    url_tables = pd.concat(url_tables, axis=0)
    test_tuples = dfu.df2str_namedtuple('htmls', url_tables)
    db.batch_replace(test_tuples)
    
    
def gen_quarter_res_urls(base_url, start_year, end_year):
    """
    start_year = 2023
    end_year = 2017
    """
    quarter_urls = []
    for year in range(start_year, end_year+1):
        for i in range(1, 5):    
            quarter_url = base_url + 'res' + str(year) + 'q{}'.format(i)
            
            if year == end_year:
                r = requests.get(quarter_url)
                bs = BeautifulSoup(r.text, 'html.parser')
                try:
                    h2 = bs.find(attrs={'class': 'subcontent'}).h2.text 
                    if h2 == "404 - File Not Found":
                        break
                except AttributeError:
                    pass
        
            quarter_urls.append(quarter_url)
    return quarter_urls


if __name__ == "__main__":
    quarter_res_urls = gen_quarter_res_urls(base_url
                                            , start_year=2017
                                            , end_year=2023)
    dump_urls_into_mysql(quarter_res_urls, tablename='cpu2017', update=False)
    
    