# -*- coding: utf-8 -*-

from __future__ import division

# 名称空间name space， 顾名思义就是存放名字的, 存什么名字呢?  比如我们定义一个变量x=1, 1是保存在内存里边的,
# 那么x保存在什么地方呢? 名称空间正式保存x与1映射关系的

def outer():
    name = 'rain'

    def inner():
        print("Print name from outer", name)

    return inner()

f = outer()
f()