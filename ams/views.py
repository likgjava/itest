import html
import json
import traceback

import datetime
import requests
import time

from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from ams.models import Api, Api_header, Api_request_param, User


def to_login(request):
    return render(request, 'login.html')


def login(request):
    userName = request.POST['userName']
    userPassword = request.POST['userPassword']

    data = {}
    try:
        user = User.objects.filter(userName=userName, userPassword=userPassword).first()
        if user:
            print('user==========', user)
            d = {'id': user.id, 'userName': user.userName}
            request.session['user'] = d
            data['code'] = '0000'
        else:
            data['code'] = '1002'
            data['msg'] = '登录失败，请检查用户名和密码是否正确！'

    except Exception as e:
        traceback.print_exc()
        data['code'] = '1001'
        data['msg'] = str(e)

    return HttpResponse(json.dumps(data), content_type="application/json")


def logout(request):
    del request.session['user']
    return redirect('/')


def to_register(request):
    return render(request, 'register.html')


def register(request):
    userName = request.POST['userName']
    userPassword = request.POST['userPassword']
    userNickName = request.POST['userNickName']

    data = {}
    try:
        user = User(userName=userName, userPassword=userPassword, userNickName=userNickName)
        user.save()
        data['code'] = '0000'
    except Exception as e:
        traceback.print_exc()
        data['code'] = '1001'
        data['msg'] = str(e)

    return HttpResponse(json.dumps(data), content_type="application/json")


def check_user_name_exist(request):
    userName = request.POST['userName']
    print('check_user_name_exist param userName={}'.format(userName))

    exists = User.objects.filter(userName=userName).exists()
    print('exists=', exists)
    data = {'valid': not exists}

    return HttpResponse(json.dumps(data), content_type="application/json")


def api_list(request):
    q = request.POST.get('q', '')
    print('api_list q={}'.format(q))

    request.session['name'] = 'likg'
    print('request.session.keys()====', request.session.keys())

    user = request.session['user']
    print('user type======', type(user))

    query = Api.objects
    if q != '':
        query = query.filter(Q(apiName__contains=q) | Q(apiURI__contains=q))
    api_list = query.order_by('-createTime')
    print('api_list======', api_list)

    # updateUser = api_list[0].updateUser
    # print('updateUser===========', updateUser.userName)

    data = {'api_list': api_list, 'total_count': len(api_list), 'q': q}
    return render(request, 'api_list.html', data)


@transaction.atomic()
def del_api(request):
    api_id = request.POST['apiId']
    print('del_api api_id={}'.format(api_id))

    Api.objects.filter(id=api_id).delete()
    Api_header.objects.filter(apiID=api_id).delete()
    Api_request_param.objects.filter(apiID=api_id).delete()

    result = {}
    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def api_detail(request):
    api_id = request.GET['apiId']
    print('api_detail api_id={}'.format(api_id))

    data = {}
    api = Api.objects.get(id=api_id)
    data['api'] = api

    header_list = Api_header.objects.filter(apiID=api_id)
    print('header_list=======', type(header_list))
    data['header_list'] = header_list

    request_param_list = Api_request_param.objects.filter(apiID=api_id)
    data['request_param_list'] = request_param_list

    return render(request, 'api_detail.html', data)


def api_test(request):
    api_id = request.GET['apiId']
    print('api_test api_id={}'.format(api_id))

    data = {}
    api = Api.objects.get(id=api_id)
    data['api'] = api

    header_list = Api_header.objects.filter(apiID=api_id)
    data['header_list'] = header_list

    request_param_list = Api_request_param.objects.filter(apiID=api_id)
    data['request_param_list'] = request_param_list

    return render(request, 'api_test.html', data)


def edit_api(request):
    api_id = request.GET['apiId']
    print('api_test api_id={}'.format(api_id))

    data = {}
    api = Api.objects.get(id=api_id)
    data['api'] = api

    header_list = Api_header.objects.filter(apiID=api_id)
    data['header_list'] = header_list

    request_param_list = Api_request_param.objects.filter(apiID=api_id)
    data['request_param_list'] = request_param_list

    return render(request, 'edit_api.html', data)


def add_api(request):
    print('add_api..................')
    data = {'name': '张三'}
    return render(request, 'add_api.html', data)


def send_request(request):
    print('send_request request param={}'.format(request.POST))
    protocol = request.POST['protocol']
    method = request.POST['method']
    uri = request.POST['uri']
    headers_str = request.POST['headers']
    params_str = request.POST['params']
    request_type = request.POST['requestType']

    global r
    result = {}
    start_time = time.time()
    try:
        headers = json.loads(headers_str)

        print('headers=====', type(headers))

        url = protocol + '://' + uri

        if method == 'GET':
            params = json.loads(params_str)
            r = requests.get(url, params=params, headers=headers)
        elif method == 'POST':
            if request_type == 'formData':
                params = json.loads(params_str)
                r = requests.post(url, params=params, headers=headers)
            else:
                r = requests.post(url, data=params_str, headers=headers)

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


def save_api(request):
    print('save_api request param={}'.format(request.POST))
    id = request.POST.get('id', None)
    protocol = request.POST['protocol']
    method = request.POST['method']
    uri = request.POST['uri']
    name = request.POST['name']
    headers_str = request.POST['headers']
    params_str = request.POST['params']
    request_type = request.POST['requestType']
    apiSuccessMock = request.POST['apiSuccessMock']
    apiFailureMock = request.POST['apiFailureMock']

    result = {}
    try:
        with transaction.atomic():
            api = Api(id=id, apiName=name, apiURI=uri, apiProtocol=protocol, apiMethod=method)
            api.apiRequestParamType = request_type
            api.apiSuccessMock = apiSuccessMock
            api.apiFailureMock = apiFailureMock
            api.createTime = datetime.datetime.now()
            api.updateUser = User(id=request.session['user']['id'])
            if request_type == 'raw':
                api.apiRequestRaw = params_str
            api.save()
            result['id'] = api.id
            print('api.id====================', api.id)

            # 如果是修改操作，则先删除历史数据
            if id is not None:
                Api_header.objects.filter(apiID=id).delete()
                Api_request_param.objects.filter(apiID=id).delete()

            headers = json.loads(headers_str)
            for k, v in headers.items():
                api_header = Api_header(headerName=k, headerValue=v, apiID=api.id)
                api_header.save()

            # a = 1 / 0

            if request_type == 'formData':
                params = json.loads(params_str)
                for k, v in params.items():
                    api_request_param = Api_request_param(paramName=k, paramValue=v, apiID=api.id)
                    api_request_param.save()

        result['success'] = True
    except Exception as e:
        result['success'] = False
        traceback.print_exc()

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


######################################################test##########################################################
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

    return render(request, 'z_bak.html', data)


def api2(request):
    list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    data = {'name': '张三', 'list': list, 'info_dict': info_dict}

    return render(request, 'z_bak2.html', data)
