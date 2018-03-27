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


class Api_group(models.Model):
    groupName = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=False)


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
    group = models.ForeignKey(Api_group, on_delete=False)
    createTime = models.DateTimeField(auto_now_add=False)


class Api_header(models.Model):
    headerName = models.CharField(max_length=255)
    headerValue = models.TextField(max_length=2000)
    apiID = models.IntegerField()


class Api_request_param(models.Model):
    paramName = models.CharField(max_length=255)
    paramValue = models.CharField(max_length=255)
    apiID = models.IntegerField()


class Test_case_group(models.Model):
    groupName = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=False)


class Test_case(models.Model):
    caseName = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=False)
    group = models.ForeignKey(Test_case_group, on_delete=False)
    updateTime = models.DateTimeField()
    createTime = models.DateTimeField(auto_now_add=False)


class Test_case_item(models.Model):
    caseData = models.CharField(max_length=255)
    statusCode = models.CharField(max_length=255)
    apiName = models.CharField(max_length=255)
    apiUri = models.CharField(max_length=255)
    apiMethod = models.CharField(max_length=255)
    apiProtocol = models.CharField(max_length=255)
    matchType = models.IntegerField()
    matchRule = models.CharField(max_length=255)
    case = models.ForeignKey(Test_case, on_delete=models.CASCADE)


class Test_case_item_result(models.Model):
    resultData = models.CharField(max_length=255)
    success = models.IntegerField()
    item = models.ForeignKey(Test_case_item, on_delete=models.CASCADE)
