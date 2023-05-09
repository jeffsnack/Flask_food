from shopeescraper import shopee
from flask import Flask, redirect, url_for, render_template,request
import requests
import json
import pandas as pd
import time
# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import re
import random
from shopee_effect import effect
from shopee_pie import shopeepie
from shopee_price import price
from shopee_smell import smell
from shopee_element import element
from shopee_flavor import flavor
from shopee_other import other
from jinja2.utils import markupsafe



app=Flask(__name__) #__name__ 代表目前執行模組
app.static_folder = 'static'

@app.route("/",methods=["GET","POST"]) # 函式的裝飾，提供附加功能
def home():
    #d=effect()
    #c=d.pie_rich_label()
    #data_plot = markupsafe.Markup(c.render_embed())
    return render_template('index.html')#,data_plot=data_plot)  

@app.route("/fb")
def fbhome():
    return render_template('fb.html')

@app.route("/shopee",methods=["GET","POST"])
def shoppehome():
    if request.method=="POST":
        mess = request.form['page']    #return mess
        d=shopee('益生菌',mess)
        d.scraper()
        df1 = pd.read_csv('益生菌_商品資料.csv')
        return 
    return render_template('shopee.html')

@app.route("/shopee/0",methods=["GET","POST"]) # 函式的裝飾，提供附加功能
def shopee_0():
    return render_template('shopeecloud.html')


@app.route("/shopee/1",methods=["GET","POST"]) # 函式的裝飾，提供附加功能
def shopee_1():
    d=shopeepie()
    c=d.pie_rich_label()
    data_plot = markupsafe.Markup(c.render_embed())
    return render_template('shopee.html',data_plot=data_plot)

@app.route("/shopee/2",methods=["GET","POST"]) # 函式的裝飾，提供附加功能
def shopee_2():
    d=effect()
    c=d.pie_rich_label()
    data_plot = markupsafe.Markup(c.render_embed())
    return render_template('shopee.html',data_plot=data_plot)

@app.route("/shopee/3",methods=["GET","POST"]) # 函式的裝飾，提供附加功能
def shopee_3():
    d=element()
    c=d.pie_rich_label()
    data_plot = markupsafe.Markup(c.render_embed())
    return render_template('shopee.html',data_plot=data_plot)

@app.route("/shopee/4",methods=["GET","POST"]) # 函式的裝飾，提供附加功能
def shopee_4():
    d=smell()
    c=d.pie_rich_label()
    data_plot = markupsafe.Markup(c.render_embed())
    return render_template('shopee.html',data_plot=data_plot)

@app.route("/shopee/5",methods=["GET","POST"]) # 函式的裝飾，提供附加功能
def shopee_5():
    d=flavor()
    c=d.pie_rich_label()
    data_plot = markupsafe.Markup(c.render_embed())
    return render_template('shopee.html',data_plot=data_plot)

@app.route("/shopee/6",methods=["GET","POST"]) # 函式的裝飾，提供附加功能
def shopee_6():
    d=price()
    c=d.pie_rich_label()
    data_plot = markupsafe.Markup(c.render_embed())
    return render_template('shopee.html',data_plot=data_plot)

@app.route("/shopee/7",methods=["GET","POST"]) # 函式的裝飾，提供附加功能
def shopee_7():
    d=other()
    c=d.pie_rich_label()
    data_plot = markupsafe.Markup(c.render_embed())
    return render_template('shopee.html',data_plot=data_plot)    




if __name__ == '__main__':#如果以主程式啟動
    app.debug = True
    app.run() #立刻啟動伺服器



