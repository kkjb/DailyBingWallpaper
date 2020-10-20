# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:27:10 2019

@author: kkjb
"""

import bing
import os
import sys

path = os.path.split(os.getcwd())[0]
path = path+"\\home"
if not os.path.exists(path):
    print ('    提示：文件夹', path, '不存在，重新建立', '\n')
    os.makedirs(path)

bing.bing_wallpaper_downloader(path,'zh-cn','1920x1080')
bing.bing_wallpaper_downloader(path,'zh-cn','1080x1920')
bing.bing_wallpaper_downloader(path,'zh-cn','1920x1200')
bing.bing_wallpaper_downloader(path,'zh-cn','UHD')
