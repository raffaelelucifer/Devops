# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class ProductInfo(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name=u"产品名称")
    leader = models.CharField(max_length=50, null=False, verbose_name=u"技术经理")
    phonenumber = models.CharField(max_length=20, null=True, verbose_name=u"联系方式")
    description = models.TextField(verbose_name=u"产品描述")

    class Meta:
        verbose_name = u"产品信息表"
        verbose_name_plural = verbose_name
        db_table = "ProductInfo"

class ProjectInfo(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name=u"项目名称")
    belongproduct = models.CharField(max_length=200, null=False, verbose_name=u"所属产品线")
    leader = models.CharField(max_length=50, null=False, verbose_name=u"项目经理")
    phonenumber = models.CharField(max_length=20, null=False, verbose_name=u"联系方式")
    server = models.CharField(max_length=200, null=False, verbose_name=u"运行服务器")
    description = models.TextField(verbose_name=u"项目描述")

    class Meta:
        verbose_name = u"项目信息表"
        verbose_name_plural = verbose_name
        db_table = "ProjectInfo"

class HostInfo(models.Model):
    ip = models.CharField(max_length=20, null=False, verbose_name=u"主机IP")
    hostname = models.CharField(max_length=30, verbose_name=u'主机名')
    port = models.CharField(max_length=10, null=False, verbose_name=u"登录端口")
    user = models.CharField(max_length=30, null=False, verbose_name=u"登录用户")
    ssh_key = models.CharField(max_length=124, null=False, verbose_name=u"登录秘钥")
    system_version = models.CharField(max_length=200, null=False, verbose_name=u"操作系统版本")
    sn = models.CharField(max_length=100, null=False, verbose_name=u"设备序列号")
    mac = models.CharField(max_length=100, null=False, verbose_name=u"设备物理地址")
    #live_port = models.CharField(max_length=200, verbose_name=u"存活端口", default="")
    host_type = models.CharField(max_length=200, null=False, verbose_name=u"主机类型")

    class Meta:
        verbose_name = u"初始化扫描信息表"
        verbose_name_plural = verbose_name
        db_table = "HostInfo"

class DockerInfo(models.Model):
    hostname = models.CharField(max_length=30, null=False, verbose_name=u"操作系统主机名")
    ip = models.CharField(max_length=20, null=False, verbose_name=u"所属机器的ip")
    docker_id = models.CharField(max_length=30, null=False, verbose_name=u"容器ID")
    port = models.CharField(max_length=10, null=True, verbose_name=u"映射端口")
    #name = models.CharField(max_length=50, null=False, verbose_name=u"容器名")
    service = models.CharField(max_length=50, null=False, verbose_name=u"运行服务")

    class Meta:
        verbose_name = u"Docker容器信息表"
        verbose_name_plural = verbose_name
        db_table = "DockerInfo"

