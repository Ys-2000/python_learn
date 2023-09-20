from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import userInfo,Department

@csrf_exempt    # csrf_exempt装饰器来排除CSRF检查
def index(request):
    print(request.method)
    print(request.GET)
    print(request.POST)
    return HttpResponse("hheo")


def user_list(request):
    return render(request, "user_list.html")


@csrf_exempt
def user_add(request):
    # redirect 重定向
    # return redirect("https://www.baidu.com/")
    return redirect("/index")



@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        # print(request.method)
        # print(request.POST)
        user = request.POST.get("name")
        pwd = request.POST.get("password")
        if user == "qwe" and pwd =="123":
            # return HttpResponse("登录成功")
            return render(request, "user_list.html", {"msg": user})
        else:
            return HttpResponse("账号或密码错误")


def orm(request):
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="人事部")
    # Department.objects.create(title="IT部")
    # userInfo.objects.create(name="qwe",password = "wqe", age = "18")
    # user = userInfo.objects.get(id=2)
    user = userInfo.objects.all()
    # user.name= "qwwe"
    # user.age= 23
    # user.save()           # 修改后需要save(),否则数据库不生效
    # user.delete()           # 删除
    print(user)
    return HttpResponse(user)