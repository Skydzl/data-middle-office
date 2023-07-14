#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 15:43:07 2023

@author: zby
"""
import re
import warnings
import requests
from bs4 import BeautifulSoup
import pandas as pd
from utils.db import DB
import utils.df as dfu
from utils.log import Log
from unify_field import get_db_field_name


db = DB('spec2017')
logger = Log('crawl')
warnings.filterwarnings('ignore')


def get_urls_from_db(tablename):
    url_info = db.select_df("""select url from htmls
                            where tablename = '{}'""".format(tablename))
    return url_info['url']


def get_benchmark(string):
    if string == "CPU2017 Integer Rate Result":
        return 'CINT2017rate'
    elif string == "CPU2017 Floating Point Speed Result":
        return 'CFP2017'
    elif string == "CPU2017 Floating Point Rate Result":
        return 'CFP2017rate'
    elif string == "CPU2017 Integer Speed Result":
        return 'CINT2017'
    else:
        raise ValueError
    

def crawling(urls, total_nums, batch_size, start_batch_i=1):
    cols = get_db_field_name(tablename='cpu2017')
    crawl_res_df = pd.DataFrame(data=None, columns=cols)
    cnt, batch_cnt = 1, 1
    batch_i = 1
    for url in urls:
        if batch_i >= start_batch_i:
            url_info = {}
            r = requests.get(url)
            bs = BeautifulSoup(r.text, 'html.parser')
            
            url_info['benchmark'] = bs.title.text.split(':')[0]
            url_info['benchmark'] = get_benchmark(url_info['benchmark'])
    
            systembar = bs.find(attrs={'class': 'systembar'})
            systembar_p = systembar.find_all('p')
            url_info['hardware_vendor'] = systembar_p[0].text.rstrip().split('\n')[0]
            url_info['sys'] = systembar_p[1].text.replace('\n', ' ').rstrip()
            
            metricbar_base = bs.find(attrs={'class': 'metricbar base'})
            metricbar_peak = bs.find(attrs={'class': 'metricbar peak'})
            if url_info['benchmark'].endswith('rate'):
                peak_results = metricbar_peak.find_all(attrs={'class': "value"})
                base_results = metricbar_base.find_all(attrs={'class': "value"})
                url_info['base_result'] = float(base_results[0].text) / 100
                url_info['peak_result'] = peak_results[0].text  
                
                if url_info['peak_result'] == 'Not Run':
                    url_info['peak_result'] = 0
                else:
                    url_info['peak_result'] = float(url_info['peak_result']) / 100
            else:
                url_info['peak_result'] = metricbar_peak.find(attrs={'class': "value"}).text
                if url_info['peak_result'] == 'Not Run':
                    url_info['peak_result'] = 0
                else:
                    url_info['peak_result'] = float(url_info['peak_result'])
                
                url_info['base_result'] = float(metricbar_base.find(attrs={'class': "value"}).text)
                
            if 'energy' in metricbar_base.text:      
                url_info['energy_base_result'] = float(base_results[1].text)
                url_info['energy_peak_result'] = peak_results[1].text 
            
                if url_info['energy_peak_result'] in ('Not Run', '--'):
                    url_info['energy_peak_result'] = 0
                else:
                    url_info['energy_peak_result'] = float(url_info['energy_peak_result'])
            else:
                url_info['energy_peak_result'] = 0
                url_info['energy_base_result'] = 0  
            
            hardware_table = bs.find(attrs={'id': 'Hardware'}).find('tbody').find_all('td')
            cores_and_chips = hardware_table[3].text.split(',')
            url_info['cores'] = cores_and_chips[0].lstrip().split(' ')[0]
            url_info['chips'] = cores_and_chips[1].lstrip().split(' ')[0]
            
            if len(cores_and_chips) > 2:
                url_info['enabled_threads_per_core'] = int(cores_and_chips[2].lstrip()[0])
            else:
                url_info['enabled_threads_per_core'] = 1
                
            url_info['processor'] = hardware_table[0].text.rstrip()
            url_info['processor_mhz'] = hardware_table[2].text
            url_info['cpu_orderable'] = hardware_table[4].text
            
            software_table = bs.find(attrs={'id': 'Software'}).find('tbody').find_all('td')
            url_info['parallel'] = software_table[2].text
            url_info['base_pointer_size'] = software_table[6].text
            url_info['peak_pointer_size'] = software_table[7].text
            url_info['first_level_cache'] = hardware_table[5].text
            url_info['second_level_cache'] = hardware_table[6].text
            url_info['third_level_cache'] = hardware_table[7].text.replace('\n', ' ')
            url_info['other_cache'] = hardware_table[8].text
            url_info['memory'] = hardware_table[9].text.replace('\n', ' ')
            url_info['storage'] = hardware_table[10].text
            url_info['operating_system'] = software_table[0].text.replace('\n', ' ')
            url_info['file_system'] = software_table[4].text
            url_info['compiler'] = software_table[1].text.replace('\n', ' ')
            
            datebar = bs.find(attrs={'class': 'datebar'}).find('tbody')
            url_info['hw_avail'] = datebar.find(attrs={'id': 'hw_avail_val'}).text
            url_info['sw_avail'] = datebar.find(attrs={'id': 'sw_avail_val'}).text
            url_info['license'] = datebar.find(attrs={'id': 'license_num_val'}).text
            url_info['tested_by'] = datebar.find(attrs={'id': 'tester_val'}).text
            url_info['test_sponsor'] = datebar.find(attrs={'id': 'test_sponsor_val'}).text
            url_info['test_date'] = datebar.find(attrs={'id': 'test_date_val'}).text
            
            notesfooter = bs.find_all(attrs={'class': 'notes footer'})[-1].text
            published = re.findall('published on [0-9]{4}-[0-1][0-9]-[0-3][0-9]', notesfooter)[0]
            url_info['published'] = re.findall('[0-9]{4}-[0-1][0-9]-[0-3][0-9]', published)[0]
            updated = re.findall('Report generated on [0-9]{4}-[0-1][0-9]-[0-3][0-9]', notesfooter)[0]
            url_info['updated'] = re.findall('[0-9]{4}-[0-1][0-9]-[0-3][0-9]', updated)[0]
    
            url_info['disclosure'] = url
            url_info['disclosures'] = ''
            crawl_res_df = crawl_res_df.append(url_info, ignore_index=True)
        
        if batch_cnt >= batch_size:
            if batch_i >= start_batch_i:
                logger.info('将第{}个batch存入数据库...'.format(str(batch_i)))
                test_tuples = dfu.df2str_namedtuple('cpu2017_crawl', crawl_res_df)
                db.batch_replace(test_tuples)
                crawl_res_df = pd.DataFrame(data=None, columns=cols)
            batch_cnt = 0
            batch_i += 1
        
        if total_nums is not None:
            if cnt >= total_nums:
                return 
        
        cnt += 1
        batch_cnt += 1
    return


if __name__ == "__main__":
    urls = get_urls_from_db(tablename='cpu2017')
    crawl_res_df = crawling(urls, total_nums=None, batch_size=16, start_batch_i=150)




