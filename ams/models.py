from django.db import models


# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=60)
    userPassword = models.CharField(max_length=60)
    userNickName = models.CharField(max_length=16)


class Project(models.Model):
    projectName = models.CharField(max_length=255)
    projectUpdateTime = models.DateTimeField()
    projectVersion = models.CharField(max_length=6)


class Api(models.Model):
    apiName = models.CharField(max_length=255)
    apiURI = models.CharField(max_length=255)
    apiProtocol = models.CharField(max_length=10)
    apiMethod = models.CharField(max_length=10)
    apiRequestParamType = models.CharField(max_length=20)
    apiRequestRaw = models.TextField(max_length=2000)
    apiSuccessMock = models.TextField()
    apiFailureMock = models.TextField()
    updateTime = models.DateTimeField()
    # updateUserID = models.IntegerField()
    # updateUser = models.ForeignKey(User, on_delete=False, db_column='updateUserID')
    updateUser = models.ForeignKey(User, on_delete=False)
    project = models.ForeignKey(Project, on_delete=False)
    createTime = models.DateTimeField(auto_now_add=False)


class Api_header(models.Model):
    headerName = models.CharField(max_length=255)
    headerValue = models.TextField(max_length=2000)
    apiID = models.IntegerField()


class Api_request_param(models.Model):
    paramName = models.CharField(max_length=255)
    paramValue = models.CharField(max_length=255)
    apiID = models.IntegerField()
