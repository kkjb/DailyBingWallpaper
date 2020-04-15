# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:39:01 2020

@author: kkjb
"""

import datetime

def gen_dates(b_date, days):
    day = timedelta(days=1)
    for i in range(days):
        yield b_date + day*i


def get_date_list(start=None, end=None):
    """
    获取日期列表
    :param start: 开始日期
    :param end: 结束日期
    :return:
    """
    if start is None:
        start = datetime.strptime("2000-01-01", "%Y-%m-%d")
    if end is None:
        end = datetime.now()
    data = []
    for d in gen_dates(start, (end-start).days):
        data.append(d)
    return data

if __name__ == "__main__":
    print(get_date_list())
