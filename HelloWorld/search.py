from django.http import HttpResponse
from django.shortcuts import render


# 表单
def search_form(request):
    return render(request, 'search_form.html')


# 接收请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)



