import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def hello(request):
    return HttpResponse("Hello world ! ")   # HttpResponse(): 返回文本，参数为字符串，字符串中写文本内容。如果参数为字符串里含有 html 标签，也可以渲染。


def base_view(request):
    return render(request, 'post.html')  # render(): 返回文本，第一个参数为 request，第二个参数为字符串（页面名称），第三个参数为字典（可选参数，向页面传递的参数：键为页面参数名，值为views参数名）。


def login(request):
    if request.method == "GET":
        return HttpResponse("cainiao")
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username =='菜鸟'and pwd =='123':
            return 'hello，菜鸟'
        else:
             return render(reverse("login"))


def test(request):
    return redirect(reverse("base"))      # redirect()：重定向，跳转新页面。参数为字符串，字符串中填写页面路径，一般用于 form 表单提交后，跳转到新页面。


# def runoob(request):
#     context = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'runoob.html', context)


def runoob(request):
    pub_date = ""
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    now = datetime.datetime.now()
    views_name = "caiNIAO caiNIAO caiNIAO"
    views_list = ["cainiao01", "cainiao02", "cainiao03"]
    views_dict = {"name": "cainiao04", "age": "17", "sex":"男",}
    num = 70
    return render(request, "runoob.html", {"views_str": views_str,
                                           "time": now,
                                           "pub_date": pub_date,
                                           "name": views_name,
                                           "views_list": views_list,
                                           "views_dict": views_dict,
                                           "num": num
                                           })
