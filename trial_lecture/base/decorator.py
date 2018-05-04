# -*- coding: utf-8 -*-

from __future__ import division


def login():
    user = 'rain'
    password = 'abcd123'
    input_user = raw_input("Please input username:")
    input_passwd = raw_input("Please input password:")

    if input_user == user and input_passwd == password:
        is_successful = True

def home():
    print("home page")

def cellphone():
    print("cellphone")

def pc():
    print("pc")

def server():
    print("server")

def watch():
    print("watch")