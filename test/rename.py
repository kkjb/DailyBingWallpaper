# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:42:11 2020

@author: kkjb
"""


fo = open("filename.txt", "r")

filename_list = []
line = fo.readline() 
filename_list.append(line)              # 调用文件的 readline()方法 
while line: 
    line = fo.readline() 
    filename_list.append(line)
 
fo.close()  

length = len(filename_list)
for a in range(0,length):
    new_name = filename_list[a].replace("_","-",2)
    filename_list[a] = new_name

fw = open("newname.txt", "w")
for name in filename_list:
    fw.write(name)
    #fw.write("\n") 
fw.close()