from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    data = {'name': '张三', 'list': list, 'info_dict': info_dict}

    return render(request, 'index.html', data)


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
