# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:32:44 2020

@author: kkjb
"""


#use for downloading bing wallpaper from https://bing.penbeat.cn/

import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time
import socket

socket.setdefaulttimeout(30)

date_suffix = "20150128"

# 文件夹不存在就创建
def create_404_dir(dirname):

    if not os.path.exists(dirname):
        print ('    提示：文件夹', dirname, '不存在，重新建立', '\n')
        os.makedirs(dirname)

#输入日期字符串 可行域 "20150128" - 至今
def get_img_url(date_suffix):
    #浏览器
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
    raw_url = "https://bing.penbeat.cn/archives/zh-CN/"
    #加上日期后缀
    url =  raw_url + date_suffix
    source_data_text = requests.get(url, headers=headers)
    soup = BeautifulSoup(source_data_text.content, 'html.parser')
    items = soup.find_all('img')
    img_url = items[0].attrs['src']
    img_url = img_url.replace("1366x768","1920x1080")
    return img_url

#分辨列替换，输入（图片地址，分辨率)
def resolution_replace(img_url, resolution):
    img_url = img_url.replace("1920x1080",resolution)
    return img_url

def reconnected_download(img_url,filepath):
    try:
        urllib.request.urlretrieve(img_url,filepath)
    except socket.timeout:
        count = 1
        while count <= 5:
            try:
                urllib.request.urlretrieve(img_url,img_url)                                                
                break
            except socket.timeout:
                err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                print(err_info)
                count += 1
        if count > 5:
            print("download job failed!")    
    
def save_img(date_suffix , img_url , dirname , resolution = "1920x1080"):
    #分辨率替换
    img_url = resolution_replace(img_url,resolution)
    img_url = img_url.replace("https","http")
    year = date_suffix[0:4]
    month = date_suffix[4:6]
    day = date_suffix[6:8]
    dirname = dirname + "/" + year 
    dirname = dirname + "/" + month
    dirname = dirname + "/" + resolution
    create_404_dir(dirname)
    
    try:
        # 用日期命名图片文件名，包括后缀 
        basename = year + "_" + month + "_" + day + "_" + resolution +"_"+ "ZH-CN" + ".jpg"
        # 拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        # 下载图片，并保存到文件夹中
        #urllib.request.urlretrieve(img_url,filepath)
        reconnected_download(img_url,filepath)
    except IOError as e:
        print('    错误：文件操作失败', e, '\n')
    except Exception as e:
        print('    错误：', e, '\n')
    else:
        print("    保存", filepath, "成功！", '\n')
        
    return filepath


        

def save_bing_wallpaper(date_suffix , dirname , resolution):
    
    
    create_404_dir(dirname)
    
    print("壁纸将被保存在：", dirname, '\n')
    img_url = get_img_url(date_suffix)
    
    if img_url != False:
        print('图片地址为：', img_url, '\n')
        save_img(date_suffix,img_url,dirname,resolution)   # 图片文件的的路径
    
    
    
    
