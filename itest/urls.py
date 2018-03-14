"""itest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ams import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('add/', views.add),
    path('add2/<int:a>/<int:b>/', views.add2),
    path('api/', views.api),
    path('api2/', views.api2),
    path('add_api/', views.add_api),
    path('send_request/', views.send_request),
    path('p/', views.p),
    path('save_api2/', views.save_api2),
    path('save_api/', views.save_api),
    path('api_list/', views.api_list),
    path('del_api/', views.del_api),
    path('edit_api/', views.edit_api),
    path('api_detail/', views.api_detail),
    path('api_test/', views.api_test),
]
