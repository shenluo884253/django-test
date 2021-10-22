from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import *
import json
def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    context= {}
    context['hello'] = 'Hello World!'
    context["name"]=[1,2,3,4,5]
    context["ahref"]="<a href='https://www.runoob.com/'>点击跳转</a>"
    return render(request, 'runoob.html', context)

def checkLogin(request):
    r=json.loads(request.body)
    request_user=r.get("user")
    try:
        u1=user.objects.get(user=request_user)
        if u1.password==r.get("pwd"):
            return HttpResponse('{"code":200,"message":"success"}')
        else:
            return HttpResponse("<p>login failed</p>")
    except:
        return HttpResponse("<p>用户名不存在</p>")

def addUser(request):
    body=json.loads(request.body)
    account=body.get("user")
    pwd=body.get("pwd")
    if account is not None:
        try:
            test1=user(user=account,password=pwd)
            test1.save()
            res={"code":200,"message":"success"}
            return HttpResponse(json.dumps(res))
        except:
            return HttpResponse(json.dumps({"code":200100,"message":u"add failed"}))

def updateUser(request):
    rq=json.loads(request.body)
    if rq["id"]==0:
        return addUser(request)
    else:
        try:
            conn=user.objects.filter(user=rq['user']).first()
            conn.pwd=rq.get("pwd")
            conn.save()
            return HttpResponse(json.dumps({"code":200,"message":u"update success"}))
        except:
            return HttpResponse(json.dumps({"code":200100,"message":u"update failed"}))






