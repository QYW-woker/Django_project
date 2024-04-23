from django.shortcuts import render

# Create your views here.
"""
视图函数：就是python函数
    视图函数的第一个参数：request
    视图函数必须返回一个响应
"""
from django.http import HttpRequest
from django.http import HttpResponse


def index(request):
    return HttpResponse("欢迎进入首页")
