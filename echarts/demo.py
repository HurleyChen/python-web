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


url = "http://api.heclouds.com/devices/26404242/datapoints?limit=5"
kv = {"api-key": "5qSAiX=uIYUNm1u7mVwM9FN=ulc="}
@app.route('/showdata/',methods=["GET","POST"])
def showdata():
    r = requests.get(url, headers=kv)
    print(r.text)
    json_str = json.loads(r.text)
    id_kind = []
    id_datagroup = []
    humi = []
    temp = []
    time = []
    count = 0
    for count in range(2):
        id_kind.append(json_str['data']['datastreams'][count]["id"])
        id_datagroup.append(json_str['data']['datastreams'][count]["datapoints"])

    print(json_str['data']['count'])
    count = 0
    for count in range(5):
        humi.append(id_datagroup[1][count]["value"])
        temp.append(id_datagroup[0][count]["value"])
        time.append(id_datagroup[0][count]["at"])
    print(humi)
    print(temp)

    if request.method=='GET':
            return render_template('showdata.html',humi = humi,temp = temp,time=time)
    else:
            pass




if __name__ == "__main__":
    # 运行项目
    app.run(debug=True)
