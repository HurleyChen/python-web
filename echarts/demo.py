# coding:utf-8

from flask import Flask, render_template, url_for,request
import requests
import json

# 生成Flask实例
app = Flask(__name__)


@app.route('/')
def my_echart():
    # 在浏览器上渲染my_templaces.html模板
    return render_template('my_template.html')

@app.route('/login/',methods=["GET","POST"])  #
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        pass

@app.route('/regist/',methods=["GET","POST"])  #
def regist():
    if request.method=='GET':
        return render_template('regist.html')
    else:
        pass


url = "http://api.heclouds.com/devices/26404242/datapoints"
kv = {"api-key": "5qSAiX=uIYUNm1u7mVwM9FN=ulc="}
@app.route('/showdata/',methods=["GET","POST"])
def showdata():
    r = requests.get(url, headers=kv)
    print(r.text)
    json_str = json.loads(r.text)
    datapoints_te = []
    datapoints= []
    data_ids = []
    count = 0
    for count in range(json_str['data']['count']):
        datapoints.append(json_str['data']['datastreams'][count]["datapoints"][0]['value'])
        data_ids.append(json_str['data']['datastreams'][count]["id"])
    print(datapoints)


    if request.method=='GET':

        return render_template('showdata.html',datapoints=datapoints)
    else:
        pass




if __name__ == "__main__":
    # 运行项目
    app.run(debug=True)
