import html
import json
import traceback

import requests
import time
from django.http import HttpResponse
from django.shortcuts import render


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
    headers_str = request.POST['headers']
    params_str = request.POST['params']

    print('params 1111111111111111111111111===========', type(params_str))

    print('protocol={} method={} uri={} name={} headers={} params={}'.format(protocol, method, uri, name, headers_str,
                                                                             params_str))
    global r
    result = {}
    start_time = time.time()
    try:
        headers = json.loads(headers_str)
        params = json.loads(params_str)
        print('headers=====', type(headers))

        url = protocol + '://' + uri

        if method == 'GET':
            r = requests.get(url, params=params, headers=headers)
        elif method == 'POST':
            r = requests.post(url, params=params, headers=headers)

        print('r=============', r)
        print('status============', r.status_code)
        result['httpCode'] = r.status_code

        result['body'] = html.escape(r.content.decode())
        result_headers = {}
        for k, v in r.headers.items():
            result_headers[k] = v
        result['headers'] = result_headers


    except Exception as e:
        result['httpCode'] = 500
        result['body'] = str(e)
        print('error.......................111111111111111111............', traceback.format_exc())
    finally:
        end_time = time.time()
        result['takeTime'] = int((end_time - start_time) * 1000)

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def add(request):
    print('add================{}'.format(request.GET))
    # aa = request.GET['aa']
    # print('aa======={}'.format(aa))
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = a + b
    return HttpResponse(str(c))


def p(request):
    # print('p======================={}'.format(dir(request.POST)))
    print('p====body=============={}'.format(request.body))
    return HttpResponse('aaaa')


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
