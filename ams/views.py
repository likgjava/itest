import html
import json
import re
import traceback

import datetime
import requests
import time

from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from ams.models import Api, Api_header, Api_request_param, User, Project, Test_case_group, Test_case, Test_case_item, \
    Api_group, Test_case_item_result


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
    print('logout session={}'.format(request.session))
    del request.session['user']
    return redirect('/to_login')


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


# ######################################################################################################
# ####################################### project ##########################################################
def project_list(request):
    plist = Project.objects.all()
    data = {'project_list': plist, 'total_count': len(plist)}

    request.session['pid'] = None
    request.session['pname'] = None
    return render(request, 'project_list.html', data)


def project_info(request):
    pid = request.GET.get('pid', None)
    if pid:
        plist = Project.objects.all()
        data = {'project_list': plist}

        project = Project.objects.get(id=pid)
        data['project'] = project

        request.session['pid'] = pid
        request.session['pname'] = project.projectName
        return render(request, 'project_info.html', data)
    else:
        return HttpResponseRedirect('/project_list/')


def save_project(request):
    print('save_project request param={}'.format(request.POST))
    id = request.POST.get('id', None)
    projectName = request.POST['projectName']
    projectVersion = request.POST['projectVersion']

    result = {}
    try:
        project = Project(id=id, projectName=projectName, projectVersion=projectVersion)
        project.save()
        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        traceback.print_exc()

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def del_project(request):
    project_id = request.POST['id']
    print('del_project project_id={}'.format(project_id))

    result = {}
    try:
        with transaction.atomic():
            Project.objects.filter(id=project_id).delete()
            api_list = Api.objects.filter(project_id=project_id)
            for api in api_list:
                api_id = api.id
                Api.objects.filter(id=api_id).delete()
                Api_header.objects.filter(apiID=api_id).delete()
                Api_request_param.objects.filter(apiID=api_id).delete()
        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        result['msg'] = str(e)
        traceback.print_exc()

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


# ######################################################################################################
# ####################################### api ##########################################################
def save_api_group(request):
    print('save_api_group request param={}'.format(request.POST))
    id = request.POST.get('id', None)
    groupName = request.POST['groupName']

    result = {}
    try:
        pid = request.session['pid']
        project = Project(id=pid)
        group = Api_group(id=id, groupName=groupName, project=project)
        group.save()
        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        traceback.print_exc()

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def api_group_list(request):
    print('api_group_list request param={}'.format(request.POST))

    data = {}
    try:
        pid = request.session['pid']
        project = Project(id=pid)
        group_list = Api_group.objects.filter(project=project)
        data['group_list'] = group_list
    except Exception as e:
        traceback.print_exc()

    return render(request, 'api_group_list.html', data)


def del_api_group(request):
    id = request.POST['id']
    print('del_api_group id={}'.format(id))

    result = {}
    try:
        with transaction.atomic():
            api_list = Api.objects.filter(group=Api_group(id=id))
            for api in api_list:
                api_id = api.id
                Api.objects.filter(id=api_id).delete()
                Api_header.objects.filter(apiID=api_id).delete()
                Api_request_param.objects.filter(apiID=api_id).delete()
            Api_group.objects.filter(id=id).delete()
        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        result['msg'] = str(e)
        traceback.print_exc()

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def api_list(request):
    q = request.POST.get('q', '')
    group_id = request.GET.get('group_id', '')
    project_id = request.session['pid']
    print('api_list q={} projectId={} group_id={}'.format(q, project_id, group_id))

    user = request.session['user']
    print('user type======', type(user))

    # 获取分组数据
    data = {}
    group_list = Api_group.objects.filter(project=Project(id=project_id))
    data['group_list'] = group_list

    query = Api.objects.filter(project_id=project_id)
    if q != '':
        query = query.filter(Q(apiName__contains=q) | Q(apiURI__contains=q))
    if group_id:
        query = query.filter(group=Api_group(id=group_id))
        data['group_id'] = int(group_id)
    else:
        data['group_id'] = None
    api_list = query.order_by('-createTime')
    data['api_list'] = api_list

    # updateUser = api_list[0].updateUser
    # print('updateUser===========', updateUser.userName)

    plist = Project.objects.all().values('id', 'projectName')
    data['project_list'] = plist

    data['total_count'] = len(api_list)
    data['q'] = q

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

    plist = Project.objects.all().values('id', 'projectName')
    data['project_list'] = plist

    data['group_list'] = Api_group.objects.all()

    return render(request, 'edit_api.html', data)


def add_api(request):
    plist = Project.objects.all().values('id', 'projectName')
    data = {'project_list': plist}
    data['group_list'] = Api_group.objects.all()
    return render(request, 'add_api.html', data)


def save_api(request):
    print('save_api request param={}'.format(request.POST))
    id = request.POST.get('id', None)
    projectId = request.session['pid']
    groupId = request.POST['groupId']
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
            api.project_id = projectId
            api.apiRequestParamType = request_type
            api.apiSuccessMock = apiSuccessMock
            api.apiFailureMock = apiFailureMock
            api.createTime = datetime.datetime.now()
            api.updateUser = User(id=request.session['user']['id'])
            api.group = Api_group(id=groupId)
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


def select_api_list(request):
    print('select_api_list request param={}'.format(request.GET))
    group_id = request.GET.get('group_id', None)

    data = {}
    try:
        pid = request.session['pid']
        group_list = Api_group.objects.filter(project=Project(id=pid))
        data['group_list'] = group_list

        api_list = Api.objects.filter(project=Project(id=pid))
        if group_id:
            api_list = api_list.filter(group=Api_group(id=group_id))
            data['group_id'] = int(group_id)
        data['api_list'] = api_list


    except Exception as e:
        traceback.print_exc()

    return render(request, 'select_api_list.html', data)


# ######################################################################################################
# ####################################### test_case ####################################################
def save_group(request):
    print('save_group request param={}'.format(request.POST))
    id = request.POST.get('id', None)
    groupName = request.POST['groupName']

    result = {}
    try:
        pid = request.session['pid']
        project = Project(id=pid)
        group = Test_case_group(id=id, groupName=groupName, project=project)
        group.save()
        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        traceback.print_exc()

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def group_list(request):
    print('group_list request param={}'.format(request.POST))

    data = {}
    try:
        pid = request.session['pid']
        project = Project(id=pid)
        group_list = Test_case_group.objects.filter(project=project)
        data['group_list'] = group_list
    except Exception as e:
        traceback.print_exc()

    return render(request, 'group_list.html', data)


def del_group(request):
    id = request.POST['id']
    print('del_group id={}'.format(id))

    result = {}
    try:
        with transaction.atomic():
            case_list = Test_case.objects.filter(group=Test_case_group(id=id))
            for case in case_list:
                Test_case_item.objects.filter(case=case).delete()
                Test_case.objects.filter(id=case.id).delete()
            Test_case_group.objects.filter(id=id).delete()
        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        result['msg'] = str(e)
        traceback.print_exc()

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def case_list(request):
    q = request.POST.get('q', '')
    group_id = request.GET.get('group_id', None)
    project_id = request.session['pid']
    print('case_list q={} group_id={}'.format(q, group_id))

    user = request.session['user']
    print('user type======', type(user))

    # 获取分组数据
    data = {}
    group_list = Test_case_group.objects.filter(project=Project(id=project_id))
    data['group_list'] = group_list

    query = Test_case.objects
    if q != '':
        query = query.filter(Q(apiName__contains=q) | Q(apiURI__contains=q))
    if group_id:
        query = query.filter(group=Test_case_group(id=group_id))
        data['group_id'] = int(group_id)
    else:
        data['group_id'] = None
    case_list = query.order_by('-createTime')
    print('case_list======', case_list)

    # updateUser = api_list[0].updateUser
    # print('updateUser===========', updateUser.userName)

    plist = Project.objects.all().values('id', 'projectName')
    data['project_list'] = plist

    data['case_list'] = case_list
    data['q'] = q

    return render(request, 'case_list.html', data)


def save_case(request):
    print('save_case request param={}'.format(request.POST))
    id = request.POST.get('id', None)
    caseGroupId = request.POST['caseGroupId']
    caseName = request.POST['caseName']

    result = {}
    try:
        pid = request.session['pid']
        project = Project(id=pid)
        group = Test_case_group(id=caseGroupId)
        case = Test_case(id=id, caseName=caseName, project=project, group=group)
        case.save()
        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        traceback.print_exc()

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def case_detail(request):
    id = request.GET['id']
    print('case_detail id={}'.format(id))

    data = {}
    case = Test_case.objects.get(id=id)
    data['case'] = case

    item_list = Test_case_item.objects.filter(case=Test_case(id=id))
    data['item_list'] = item_list

    plist = Project.objects.all().values('id', 'projectName')
    data['project_list'] = plist

    return render(request, 'case_detail.html', data)


def del_case(request):
    case_id = request.POST['id']
    print('del_case case_id={}'.format(case_id))

    result = {}
    try:
        with transaction.atomic():
            Test_case_item.objects.filter(case=Test_case(id=case_id)).delete()
            Test_case.objects.filter(id=case_id).delete()
        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        result['msg'] = str(e)
        traceback.print_exc()

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def del_case_item(request):
    id = request.POST['id']
    print('del_case_item item_id={}'.format(id))

    result = {}
    try:
        with transaction.atomic():
            Test_case_item.objects.filter(id=id).delete()
        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        result['msg'] = str(e)
        traceback.print_exc()

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def to_add_case_item(request):
    caseId = request.GET['caseId']
    apiId = request.GET.get('apiId', None)
    print('to_add_case_item caseId={} apiId={}'.format(caseId, apiId))

    data = {'caseId': caseId}

    if apiId:
        api = Api.objects.get(id=apiId)
        data['api'] = api

        header_list = Api_header.objects.filter(apiID=apiId)
        data['header_list'] = header_list

        request_param_list = Api_request_param.objects.filter(apiID=apiId)
        data['request_param_list'] = request_param_list

    plist = Project.objects.all().values('id', 'projectName')
    data['project_list'] = plist

    return render(request, 'add_case_item.html', data)


def to_edit_case_item(request):
    itemId = request.GET['itemId']
    print('to_edit_case_item itemId={}'.format(itemId))

    case_item = Test_case_item.objects.get(id=itemId)
    data = {'case_item': case_item}
    data['caseId'] = case_item.case.id

    # 请求头
    caseData = json.loads(case_item.caseData)
    header_list = caseData['headers']
    data['header_list'] = header_list

    # 请求参数
    requestType = caseData['requestType']
    data['requestType'] = requestType
    if requestType == 'raw':
        data['raw'] = caseData['raw']
    data['request_param_list'] = caseData['params']

    # 校验规则
    data['match_rule_list'] = []
    if case_item.matchType == 3:
        data['match_rule_list'] = json.loads(case_item.matchRule)

    plist = Project.objects.all().values('id', 'projectName')
    data['project_list'] = plist

    print('data={}'.format(data))
    return render(request, 'edit_case_item.html', data)


def save_case_item(request):
    print('save_case_item request param={}'.format(request.POST))
    id = request.POST.get('id', None)
    caseId = request.POST.get('caseId', None)
    apiProtocol = request.POST['apiProtocol']
    apiMethod = request.POST['apiMethod']
    apiUri = request.POST['apiUri']
    apiName = request.POST['apiName']
    headers_str = request.POST['headers']
    request_type = request.POST['requestType']
    matchType = request.POST['matchType']
    statusCode = request.POST['statusCode']
    matchRule = request.POST.get('matchRule', '')

    result = {}
    try:
        caseData = {}
        caseData['headers'] = json.loads(headers_str)
        caseData['apiUri'] = apiUri
        caseData['apiProtocol'] = apiProtocol
        caseData['apiMethod'] = apiMethod
        caseData['requestType'] = request_type
        if request_type == 'raw':
            caseData['raw'] = request.POST['raw']
            caseData['params'] = []
        else:
            caseData['params'] = json.loads(request.POST['params'])

        with transaction.atomic():
            case_item = Test_case_item(id=id, apiName=apiName, apiUri=apiUri, apiProtocol=apiProtocol)
            case_item.case = Test_case(id=caseId)
            case_item.apiMethod = apiMethod
            case_item.matchType = matchType
            case_item.statusCode = statusCode
            case_item.caseData = json.dumps(caseData)
            case_item.matchRule = matchRule
            case_item.save()

        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        result['msg'] = str(e)
        traceback.print_exc()

    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def auto_test(request):
    print('auto_test request param={}'.format(request.GET))
    id = request.POST.get('id', None)
    caseId = request.POST.get('caseId', None)
    itemId = request.GET['itemId']

    result = {}
    try:

        case_item = Test_case_item.objects.get(id=itemId)
        print('case_item.caseData================================================================', case_item.caseData)

        # 构造请求头数据
        headers = {}
        caseData = json.loads(case_item.caseData)
        header_list = caseData['headers']
        for header in header_list:
            headers[header['headerName']] = header['headerValue']

        # 构造请求参数
        params = {}
        param_list = caseData['params']
        for param in param_list:
            params[param['paramName']] = param['paramValue']
        requestType = caseData['requestType']
        print('auto_test params=============================={}'.format(params))

        # 校验规则
        # data['match_rule_list'] = []
        # if case_item.matchType == 3:
        #     data['match_rule_list'] = json.loads(case_item.matchRule)

        url = case_item.apiProtocol + '://' + case_item.apiUri

        global r
        if case_item.apiMethod == 'GET':
            r = requests.get(url, params=params, headers=headers)
        elif case_item.apiMethod == 'POST':
            if requestType == 'formData':
                r = requests.post(url, params=params, headers=headers)
            else:
                r = requests.post(url, data=caseData['raw'], headers=headers)

        print('r.text============================', r.text)
        print('r.request.headers============================', r.request.headers)

        # 验证测试结果
        success = _check_test_result(case_item, r)
        result['success'] = success

        # 构建测试结果并保存
        test_result = _build_test_result(r, url, case_item, params, caseData)
        item_result = Test_case_item_result(resultData=test_result, item=case_item, success=success)
        item_result.save()

        result['item_result_id'] = item_result.id
        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        result['msg'] = str(e)
        traceback.print_exc()

    print('result==============={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def _cal_param_value(param_value, response_data_list):
    print('_cal_param_value param_value={} response_data_list={}'.format(param_value, response_data_list))
    try:
        # 格式：<response[0].sum>
        match = re.match(r'<response\[(\d*)\]\.(.*)>', param_value)
        if match:
            index = match.group(1)
            key = match.group(2)
            print('_cal_param_value index={} key={}'.format(index, key))
            response_data = response_data_list[int(index)]
            return response_data[key]
        else:
            return param_value
    except Exception as e:
        traceback.print_exc()
        return None


def auto_test_batch(request):
    print('auto_test_batch request param={}'.format(request.GET))
    caseId = request.GET.get('caseId', None)

    result = {}
    try:
        test_result_list = []
        response_data_list = []
        item_list = Test_case_item.objects.filter(case=Test_case(id=caseId))
        for item in item_list:
            print('case_item.caseData================================================================', item.caseData)

            # 构造请求头数据
            headers = {}
            caseData = json.loads(item.caseData)
            header_list = caseData['headers']
            for header in header_list:
                headers[header['headerName']] = header['headerValue']

            # 构造请求参数
            params = {}
            param_list = caseData['params']
            for param in param_list:
                paramValue = _cal_param_value(param['paramValue'], response_data_list)
                params[param['paramName']] = paramValue
            requestType = caseData['requestType']
            print('params========={}'.format(params))

            url = item.apiProtocol + '://' + item.apiUri

            global r
            if item.apiMethod == 'GET':
                r = requests.get(url, params=params, headers=headers)
            elif item.apiMethod == 'POST':
                if requestType == 'formData':
                    r = requests.post(url, params=params, headers=headers)
                else:
                    r = requests.post(url, data=caseData['raw'], headers=headers)

            # 验证测试结果
            success = _check_test_result(item, r)

            # 缓存响应结果
            response_data = _cache_response_data(item, r)
            response_data_list.append(response_data)

            # 构建测试结果并保存
            test_result = _build_test_result(r, url, item, params, caseData)
            item_result = Test_case_item_result(resultData=test_result, item=item, success=success)
            item_result.save()

            test_result = {'item_result_id': item_result.id, 'success': success}
            test_result_list.append(test_result)

        result['test_result_list'] = test_result_list
        result['code'] = '0000'
    except Exception as e:
        result['code'] = '1001'
        result['msg'] = str(e)
        traceback.print_exc()

    print('result==============={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def _cache_response_data(case_item, r):
    print('_cache_response_data matchType={}'.format(case_item.matchType))
    try:
        # 3:json校验
        if case_item.matchType == 3:
            returnBody = r.content.decode()
            return json.loads(returnBody)
    except Exception as e:
        traceback.print_exc()
        return {}


def _check_test_result(case_item, r):
    print('_check_test_result matchType={}'.format(case_item.matchType))
    try:
        # 0:不校验
        if case_item.matchType == 0:
            return True

        # 验证状态码
        if case_item.statusCode != str(r.status_code):
            print('_check_test_result rule status={} actual status={}'.format(case_item.statusCode, r.status_code))
            return False

        # 1:完全校验
        returnBody = r.content.decode()
        print('_check_test_result returnBody={} aa===================={}'.format(returnBody, returnBody == 'None'))
        if case_item.matchType == 1:
            return case_item.matchRule == returnBody

        # 2:正则校验
        if case_item.matchType == 2:
            return re.match(case_item.matchRule, returnBody) is not None

        # 3:json校验
        if case_item.matchType == 3:
            if not returnBody:
                return False
            rule_list = json.loads(case_item.matchRule)
            body = json.loads(returnBody)
            if not isinstance(body, dict):
                return False
            for rule in rule_list:
                print('_check_test_result rule={}'.format(rule))
                matchRule = rule['matchRule']
                paramKey = rule['paramKey']
                paramInfo = rule['paramInfo']
                # 无
                if matchRule == 0:
                    # if body.get(paramKey) is None:
                    #     return False
                    continue
                # 等于
                elif matchRule == 1:
                    if str(body[paramKey]) != paramInfo:
                        return False
                # 不等于
                elif matchRule == 2:
                    if str(body[paramKey]) == paramInfo:
                        return False
                # 大于
                elif matchRule == 3:
                    if str(body[paramKey]) <= paramInfo:
                        return False
                # 小于
                elif matchRule == 4:
                    if str(body[paramKey]) >= paramInfo:
                        return False
                # 正则
                elif matchRule == 5:
                    if re.match(paramInfo, str(body[paramKey])) is None:
                        return False
            return True
    except Exception as e:
        traceback.print_exc()
        return False


def _build_test_result(response, url, case_item, params, caseData):
    result = {}
    result['url'] = url
    result['apiMethod'] = case_item.apiMethod
    result['statusCode'] = response.status_code

    request_headers = {}
    for k, v in response.request.headers.items():
        request_headers[k] = v
    result['headers'] = request_headers

    result['requestType'] = caseData['requestType']
    if caseData['requestType'] == 'raw':
        result['raw'] = caseData['raw']
    result['params'] = params

    result['matchType'] = case_item.matchType
    result['matchStatusCode'] = case_item.statusCode
    if case_item.matchType == 3:
        result['matchRule'] = json.loads(case_item.matchRule)
    else:
        result['matchRule'] = case_item.matchRule

    result['returnBody'] = r.content.decode()

    print('test_result=======================', json.dumps(result))
    return json.dumps(result)


def test_result(request):
    print('test_result request param={}'.format(request.GET))
    id = request.GET['id']

    data = {}
    try:
        item_result = Test_case_item_result.objects.get(id=id)
        resultData = json.loads(item_result.resultData)
        data['resultData'] = resultData

        data['case_item'] = Test_case_item.objects.get(id=item_result.item.id)

    except Exception as e:
        traceback.print_exc()

    return render(request, 'test_result.html', data)


def bind_param(request):
    print('bind_param request param={}'.format(request.GET))
    itemId = request.GET['itemId']
    index = request.GET['index']

    data = {}
    try:
        case_item = Test_case_item.objects.get(id=itemId)
        item_list = Test_case_item.objects.filter(case=case_item.case, id__lt=itemId)
        for item in item_list:
            if item.matchType == 3:
                item.matchRule = json.loads(item.matchRule)
            else:
                item.matchRule = []
        data['item_list'] = item_list
        data['index'] = index
    except Exception as e:
        traceback.print_exc()

    return render(request, 'bind_param.html', data)


# ######################################################################################################
# #################################################### test ############################################
def add(request):
    print('add================{}'.format(request.GET))
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)

    result = {'sum': c}
    print('result={}'.format(result))
    return HttpResponse(json.dumps(result), content_type="application/json")


def sub(request):
    print('sub================{}'.format(request.GET))
    result = None
    try:
        a = request.GET['a']
        b = request.GET['b']
        result = int(a) - int(b)
    except Exception as e:
        print('sub error.', str(e))
    return HttpResponse(str(result))


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
