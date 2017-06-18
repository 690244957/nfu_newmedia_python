# -*- coding: utf-8 -*- 
import requests

import json
with open('data/guangdongmap.json','rb')as fp:
    python=json.load(fp)
    
def get_location(cities):
    z=python[cities]
    return z

#抓取地图
def get_img(cities):
    path_img = ("maps/{img}.png".format(img=cities))
    #高德地图（静态地图）api
    url_api = "http://restapi.amap.com/v3/staticmap"
    parameters={'location':'',
                'zoom':10,
                'size':'1000*600',
                'key': 'ee83ffb0500bcbbe5929a0d58d012e0e'}
    parameters['location']=get_location(cities)
    r = requests.get(url_api, params=parameters)
    try:
        data = r.json()
    except:
        data = r.content
    with open (path_img, "wb") as f:
        f.write(r.content)
    return path_img


