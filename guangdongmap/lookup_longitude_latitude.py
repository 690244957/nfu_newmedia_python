# -*- coding: utf-8 -*- 
with open ('data/guangdong.txt','r',encoding='utf8')as data:
    gd=data.readlines()


xxx=gd[0].strip().split(' ')
#print(xxx)

yyy ={x.split(':')[0]:x.split(':')[1] for x in xxx}
#print(yyy)

#print(yyy['纬度'])

line_all=[]
for line in gd:
    line_data = line.strip().split(' ')
    line_dict = {x.split(':')[0]:x.split(':')[1] for x in line_data}
    # {'经度': '111.48', '城市': '广东封开', '纬度': '23.45;'}
    line_all.append(line_dict)

line_all_dict={}
for line in gd:
    line_data = line.strip().split(' ')
    line_dict = {x.split(':')[0]:x.split(':')[1] for x in line_data}
    k=line_dict['城市']
    v= {'经度':line_dict[ '经度'], '纬度':line_dict[ '纬度']}
    line_all_dict.update({k:v})

print(line_all_dict['广东从化'])
print(line_all_dict['广东从化']['经度'])



def location(city):
   x=line_all_dict['广东从化']['经度']
   y=line_all_dict['广东从化']['纬度']


   return(x,y)


x, y = location('广东从化')
print(x,y)

import folium
map_osm = folium.Map(location=[x, y], zoom_start=14)
folium.Marker([x, y], 
              popup="广东从化", 
              icon=folium.Icon(color='red',icon='info-sign')
             ).add_to(map_osm)
map_osm.save('map.html')