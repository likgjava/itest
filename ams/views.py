from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    data = {'name': '张三', 'list': list, 'info_dict': info_dict}

    return render(request, 'index.html', data)


def add_api(request):
    print('add_api..................')
    data = {'name': '张三'}
    return render(request, 'add_api.html', data)


def send_request(request):
    print('1111111111111111111111111111111111111')
    protocol = request.POST['protocol']
    method = request.POST['method']
    uri = request.POST['uri']
    name = request.POST['name']
    headers = request.POST['headers']
    params = request.POST['params']

    print('protocol={} method={} uri={} name={} headers={} params={}'.format(protocol, method, uri, name, headers, params))


    data = {'name222': '张三'}
    return HttpResponse(data)


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = a + b
    return HttpResponse(str(c))


def api(request):
    list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    data = {'name': '张三', 'list': list, 'info_dict': info_dict}

    return render(request, 'api.html', data)


def api2(request):
    list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    data = {'name': '张三', 'list': list, 'info_dict': info_dict}

    return render(request, 'api2.html', data)
