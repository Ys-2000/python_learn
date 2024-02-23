from django.utils.deprecation import MiddlewareMixin


class Mid1(MiddlewareMixin):
    def process_request(self, request):     # 请求views方法之前会执行
        print("request请求开始")

    def process_response(self, request, response):
        print("请求处理完毕，将返回到页面！")
        return response