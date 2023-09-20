# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Hello, web!</h1>']


# environ：一个包含所有HTTP请求信息的dict对象
# start_response：一个发送HTTP响应的函数

def application(environ, start_response):
    start_response('300 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

