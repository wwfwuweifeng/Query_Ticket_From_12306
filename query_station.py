#-*- coding: utf-8 -*-
import requests
import re

def station_name():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
    text = requests.get(url, verify=False).text
    stations = re.findall(r'\|([^|]+)\|([A-Z]+)', text)
    print('i am query stations ok ')
    stations = dict(stations)
    return stations
