# -*- coding: utf-8 -*-

from __future__ import division

#  1. 函数示例
#   函数定义: 将一组语句的集合通过一个名字(函数名封装起来), 要想执行这个函数, 只需调用其函数名即可.
def sayhello():
    print("Hi, welcome to oldboy")

# 2. 函数参数
# a. 实参， 形参
def calc(x, y):     # 形参, 只在函数内部生效, 主函数调用结束后, 不能再使用函数变量
    result = x**y

    return result

# actual_res = calc(2,3)  # 实参, 必须是确定的值, 把确定的值传给行参, 这里2传给x, 3传给y
# print(actual_res) # 打印的时候，意味着调用calc函数结束, 此时内存里边不在保存x, y的变量.
# b. 默认参数
def cellphone(name,company,number,country='China'):
    print("Name:%s" % country)

# c. 关键参数(指定参数名称的参数就叫关键参数, 关键参数位置必须是按照顺序传参
def contacts(username, age, email='abc@163.com', cellphone='18610001010'):
    print("----联系人信息----")
    print("姓名:%s" % username)
    print("年龄:%s" % age)
    print("邮箱:%s" % email)
    print("手机号:%s" % cellphone)

# 这样调用是可以的
# contacts('rain',email='wangyy@163.com',age=28,cellphone='15611709090')
# # 这样调用是非法的
# contacts('rain',email='wangyy@163.com',28,cellphone='15611709090')
# # # 这样会出现重复赋值
# contacts('rain',30,age=28,cellphone='15611709090')

# d. 非固定参数(如果你在定时函数的时候, 不确定传入多少个参数, 就可以使用非固定参数)
def business_card(name, position, *args, **kwargs): # *arge会把传入的参数转换成元组，**kwagrs会把传入的参数转成字典
    print(name, position)
    print(name, position, args)
    print(name, position, args, kwargs)

# business_card('rain','architecture')
# business_card('rain','teacher','aaa','bbb','ccc')
# business_card('rain','teacher','aaa','bbb','ccc',leader='alex')

# e. 函数返回值, return
# def is_sucessful(num):
#     if num > 10:
#         return True
#     else:
#         return False
#
# res = is_sucessful(11)
# print(res)

# f. 全局变量和局部变量
# country = 'China'
# def go_aboard():
#     # print("Before:%s" % country)
#     # global country 如果在函数里边声明了country 为全局变量, 外边的变量就会修改
#     country = 'Thiland'
#     print("After:%s" % country)
#
# go_aboard() # 看到在函数里边， 重新赋值之后, country 变成Thiland
# print(country) # 但是此时函数外边的country的名称依然是 China, 要想是函数外边的country名称改变，怎么做呢?

# g. 嵌套函数
name = 'cellphone'
def products():
    name = "pc"
    def new_product():
        name = "server"
        print(name)
    new_product()
    print(name)
# products()
# products.new_product()  # 这里调用失败
# print("函数外打印%s" % name)

# h. 高阶函数, 函数的参数能接收变量, 也能接收一个函数作为参数
def sum(a, b):
    res = a + b
    return res

def test(x, y, f):

    return f(x, y)
print test(2,3,sum)
# i. 递归
# j. 内置函数
