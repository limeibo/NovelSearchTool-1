#!/usr/bin/env python
# encoding: utf-8
"""
@author: zhangjunbo@meituan.com
@time: 2017/6/18 上午12:09
@desc:
"""
import os
import zipfile
import sys
# 压缩小说
def zipBook(name):
    dire = r'{}/static/books/{}'.format(sys.path[0], name)
    z = zipfile.ZipFile(dire + ".zip", 'w')
    if os.path.isdir(dire):
        for d in os.listdir(dire):
            z.write(dire + os.sep + d, name + os.sep + d)
        z.close()
    return dire + ".zip"