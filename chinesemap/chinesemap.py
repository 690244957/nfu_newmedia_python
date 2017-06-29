# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, escape, url_for, send_file
from lookup_longitude_latitude import get_img

app = Flask(__name__)

import json  #调用json模块
with open('data/PRCmap.json','rb')as fp:  #打开data/PRCmap.json文件
    python=json.load(fp)  #读取json文件
cities=python.keys()   #变量cities=python里的键
city_list=list(cities) #建一个列表，内容是python里的键


@app.route('/pick_city', methods=['POST'])
def do_search() -> 'html':  #定义一个函数
    """Extract the posted data; perform the search; return results."""
    user_city = request.form['the_user_city']
    title = '以下是您的结果：'
    results = []  #建立一个空列表
    zoom_list=list(range(7,14,3))  #
    for y in zoom_list: #建立一个for循环
        results.append( get_img(user_city, z=y) )  #将从网页得到的信息放入get_img(),然后得到图片
    results = {zoom_list[i]:x for i,x in enumerate(results)}  
    return render_template('results.html', 
                           the_title=title,
                           the_city=user_city,
                           the_results=results)   #将图片输出到网页

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html': 
    """Display this webapp's HTML form."""
    print(city_list)
    return render_template('entry.html',
                           the_title='城市地图导航',
                           the_available_city=city_list)



#这里我们接受一个 filename 檔名变量，http://127.0.0.1:5000/img/檔名
@app.route('/maps/<filename>')  #filename
def get_image(filename):        #filename 
    #傳送mimetype="image/"
    #假定都是image/png格式
    import os.path
    
    return send_file(os.path.join("maps",filename), mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
