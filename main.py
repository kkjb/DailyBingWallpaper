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

bing.save_bing_wallpaper(path,'1920x1080','zh-cn')
bing.save_bing_wallpaper(path,'1920x1200','zh-cn')
bing.save_bing_wallpaper(path,'1080x1920','zh-cn')
bing.save_bing_wallpaper(path,'UHD','zh-cn')
