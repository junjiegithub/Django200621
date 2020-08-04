#coding =utf-8
from django.http import HttpResponse
from django.shortcuts import render

#显示一个字符串
#python manage.py runserver 127.0.0.1:8000  启动服务
def index_view(request):
#根据不同的请求方式处理不同的业务需求
    m=request.method

    if request.method=="GET":
        return render(request,'register.html')
    else:
        #1。接收请求参数
        uname = request.POST.get('uname','')
        pwd =request.POST.get('pwd','')
        #2。非空判断

        #3。创建模型对象
        #4。插入数据库
        #5。页面响应
        return HttpResponse('处理注册功能')

#显示一个登录首页

