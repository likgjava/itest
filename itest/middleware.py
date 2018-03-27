from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

no_auth_path = ['/to_login/', '/login/', '/to_register/', '/register/', '/logout/',
                '/check_user_name_exist/']


class ExteriorAuthMiddleware(MiddlewareMixin):
    # 判断登录 权限控制
    def process_request(self, request):
        print('ExteriorAuthMiddleware {} request.path={}'.format('*' * 100, request.path))
        print('ExteriorAuthMiddleware..........session.keys()={}'.format(request.session.keys()))
        if request.method == 'GET':
            requestData = request.GET
        else:
            requestData = request.POST
        request.session['errmsg'] = ''

        # 退出
        if request.path in ['/logout/']:
            print('退出系统........')
            pass
        # 未登录
        elif not request.session.has_key('user'):
            # 测试接口
            if request.path.startswith('/test/'):
                print('这是测试接口........')
                pass
            # 转到登录界面
            elif request.path not in no_auth_path:
                return HttpResponseRedirect('/to_login/')
        # 已登录
        else:
            pid = request.session.get('pid', None)
            print('pid===================================', pid)
            # 如果是登录则转到首页
            if request.path in ['/', '/to_login/']:
                return HttpResponseRedirect('/project_list/')

            # 如果还没有选择某个项目则只能进入‘项目管理’页面
            if not pid and request.path not in ['/project_list/', '/project_info/', '/save_project/', '/del_project/']:
                return HttpResponseRedirect('/project_list/')
