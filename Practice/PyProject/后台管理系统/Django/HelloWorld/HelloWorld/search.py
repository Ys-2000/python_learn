from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# 表单
def search_form(request):
    return render(request, 'search_form.html')      # render(): 返回文本，第一个参数为 request，第二个参数为字符串（页面名称），第三个参数为字典（可选参数，向页面传递的参数：键为页面参数名，值为views参数名）。



# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)        # HttpResponse(): 返回文本，参数为字符串，字符串中写文本内容。如果参数为字符串里含有 html 标签，也可以渲染。


# 使用 @csrf_exempt 装饰器，这将会禁用对该视图的CSRF保护。但是请注意，这会降低你的应用的安全性，因为这将不再验证请求的来源是否合法。这种方法只适用于非常特殊的情况。
@csrf_exempt
def runoob(request):
    name = request.POST.get("name")
    path = request.path
    method = request.method
    return HttpResponse('姓名：{} 路径：{} 请求方法:{}'.format(name, path, method))

