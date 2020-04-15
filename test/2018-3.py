# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:30:35 2020

@author: kkjb
"""

import datetime
import old_wall
import os
path = os.path.split(os.getcwd())[0]
path = path+"\\home"

#generate time str in format of yyyymmdd
def create_assist_date(datestart = None,dateend = None):
	# 创建日期辅助表

	if datestart is None:
		datestart = '20180701'
	if dateend is None:
		dateend = '20180930'

	# 转为日期格式
	datestart=datetime.datetime.strptime(datestart,'%Y%m%d')
	dateend=datetime.datetime.strptime(dateend,'%Y%m%d')
	date_list = []
	date_list.append(datestart.strftime('%Y%m%d'))
	while datestart<dateend:
		# 日期叠加一天
	    datestart+=datetime.timedelta(days=+1)
	    # 日期转字符串存入列表
	    date_list.append(datestart.strftime('%Y%m%d'))
	return date_list

(date_list) = create_assist_date()

for date in date_list:

    old_wall.save_bing_wallpaper(date, path ,'1080x1920')
    old_wall.save_bing_wallpaper(date, path ,'1920x1080')
    old_wall.save_bing_wallpaper(date, path ,'1920x1200')