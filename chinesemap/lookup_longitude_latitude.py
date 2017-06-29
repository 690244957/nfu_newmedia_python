# -*- coding: utf-8 -*- 
import requests
import json

def download():  #定义dowloand函数
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
    _cities={}
    for i in range(len(F)):
        _cities[F[i]]=T[i]
    return(_cities)
    

    
try:
    with open('data/chinesemap.json','r') as fp:
        PRC_cities = json.load(fp)    #尝试打开并读取data/chinesemap.json
except:
    PRC_cities = download()      
    with open('data/chinesemap.json','w') as file:
        json.dump(PRC_cities, file)   #如若不行则打开data/chinesemap#


  
#抓取地图
def get_img(a_city, z='10'):   #定义get_img函数，并且可以输入a_city, z='10'
    path_img = "maps/{img}_{zo}.png".format(img=a_city, zo=z)
    #高德地图（静态地图）api
    url_api = "http://restapi.amap.com/v3/staticmap"  #api网址
    parameters={'location':'',
                'zoom':z,
                'size':'1000*600',
                'key': 'ee83ffb0500bcbbe5929a0d58d012e0e'}   #调用api参数
    
    parameters['location']= PRC_cities[a_city]
    r = requests.get(url_api, params=parameters)   #调用api
    try:
        data = r.json()  #尝试打开json档
    except:
        data = r.content #如果打不开就输出api的原始数据
    with open (path_img, "wb") as f:
        f.write(r.content)  #将地图的代码输出成图片文件
    return path_img   #返回图片

