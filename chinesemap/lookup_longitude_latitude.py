# -*- coding: utf-8 -*- 
import requests

import json

#中国各省经纬度资料抓取
url_api = "http://restapi.amap.com/v3/config/district"
parameters = {'keywords': '中华人民共和国', 
              'subdistrict': 2,
              'key': 'ee83ffb0500bcbbe5929a0d58d012e0e'}
r = requests.get (url_api, params=parameters)
data = r.json()

ans09 ={ x['name']: [y['name'] for y in x['districts']] for x in data['districts'][0]['districts'] }
l = [[kk+x for x in ll] for kk,ll in ans09.items()]
F=[y for sublist in l for y in sublist]
ans10 ={ x['name']: [y['center'] for y in x['districts']] for x in data['districts'][0]['districts']}
R=ans10.values()
Z=list(R)
T=[y for x in Z for y in x]
dict={}
for i in range(len(F)):
    dict[F[i]]=T[i]
    
with open('data/chinesemap.json','w') as file:
    json.dump(dict,file)
    
with open('data/chinesemap.json','r')as fp:
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


