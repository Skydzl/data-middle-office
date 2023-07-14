# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 12:28:48 2022

@author: zhangboyu_sx
"""
import json
import requests

# 用POST方式测试接口
pvod_data = {'title': '极限保镖',
        'online_date': '2023-12-01',
        'tag': '奇幻|动作|爱情', 
        'stars': '安志杰|薛凯琪|伍允龙|林家栋',
        'directors': '李子俊|吕冠南',
        'writers': '吕冠南',
        'size': '中',
        'years': '永久',
        'saidao': '警匪犯罪',
        'level': '过亿',
        'quanceng': '男青年',
        'score': '3',
        'main_type': '动作',
        'schedule': '1',
        'holidays': '3',
        'is_holidays': '0',
        'holidays_next_gap': '28',
        'similar': '盲战',
        # 'IP_name': '奇门遁甲'
        }


data_json = json.dumps(pvod_data, ensure_ascii=True)

r = requests.post("http://127.0.0.1:5000//", data=data_json)
print(r.text)