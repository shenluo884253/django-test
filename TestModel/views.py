from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json
# Create your views here.
def zz(request):
    return HttpResponse('<p>include test</p>')

def add_zz(request):
    org_id=request.POST.get("org_id")
    name=request.POST.get("name")
    conn=models.Zhouwei(org_id=org_id,name=name)
    conn.save()
    data={"code":200,"msg":"success"}
    return HttpResponse(json.dumps(data))


def get_anog_list(request):
    data=request.body
    d=json.loads(data)
    print(d)
    return HttpResponse(data)

def get_orgids(request):
    data = request.body
    d = json.loads(data)
    print(d)
    return HttpResponse(data)
