# -*- coding: utf-8 -*-

from scanhosts import models
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import  csrf_exempt
from django.core import serializers
#from singledispatch import singledispatch
import subprocess
import json
import datetime
from decimal import Decimal

@csrf_exempt
def getnumber_of_assets(req):
    phy_number = len(models.HostInfo.objects.all())
    vir_number = len(models.DockerInfo.objects.all())
    return JsonResponse({'status': 10021, 'phy_number': phy_number, 'vir_number': vir_number})

@csrf_exempt
def getinfo_from_physical(request):
    #postbody = request.body
    #json_result = json.loads(postbody)
    #page = json_result['pag']
    context = {'status': 200}
    #context['page'] = page

    try:
        phy_info = models.HostInfo.objects.all()
    except:
        phy_info = None
    if phy_info == None:
        return JsonResponse({'status': 10021, 'message': 'There are no infomations'})
    #paginator = Paginator(phy_info_list, 10)
    #try:
    #    phy_info = paginator.page(page)
    #except PageNotAnInteger:
    #    phy_info = paginator.page(1)
    #except EmptyPage:
    #    phy_info = paginator.page(paginator.num_pages)
    #context['queryNum'], context['hasPrevios'], context['hasNext'] = len(phy_info), phy_info.has_previous(), phy_info.has_next()
    data = []
    if phy_info:
        for i in phy_info:
            phy_info_array = {}
            phy_info_array['ip'] = str(i.ip)
            phy_info_array['hostname'] = str(i.hostname)
            phy_info_array['system_version'] = i.system_version
            phy_info_array['sn'] = i.sn
            phy_info_array['mac'] = i.mac
            data.append(phy_info_array)
        context.update({'data': data})
        return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt
def getinfo_from_virtual(request):
    #postbody = request.body
    #json_result = json.loads(postbody)
    #page = json_result['pag']
    context = {'status': 200}
    #context['page'] = page

    try:
        virtual_info = models.DockerInfo.objects.all()
    except:
        virtual_info = None
    if virtual_info == None:
        return JsonResponse({'status': 10031, 'message': 'There are no infomations'})
    #paginator = Paginator(virtual_info_list, 10)
    #try:
    #    virtual_info = paginator.page(page)
    #except PageNotAnInteger:
    #    virtual_info = paginator.page(1)
    #except EmptyPage:
    #    virtual_info = paginator.page(paginator.num_pages)
    #context['queryNum'], context['hasPrevios'], context['hasNext'] = len(virtual_info), virtual_info.has_previous(), virtual_info.has_next()
    data = []
    if virtual_info:
        for i in virtual_info:
            virtual_info_array = {}
            virtual_info_array['ip'] = str(i.ip)
            virtual_info_array['hostname'] = str(i.hostname)
            virtual_info_array['docker_id'] = i.docker_id
            virtual_info_array['port'] = i.port
            virtual_info_array['service'] = i.service
            data.append(virtual_info_array)
        context.update({'data': data})
        return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt
def add_productinfo(request):
    postbody = request.body
    json_result = json.loads(postbody)
    name = json_result["name"]
    leader = json_result["leader"]
    phone = json_result["phone_number"]
    description = json_result["description"]
    try:
        product = models.ProductInfo.objects.get(name=name)
    except:
        product = None
    if product is not None:
        return JsonResponse({'status': 10011, 'messages':"The product is already exist."})
    else:
        models.ProductInfo.objects.create(name = name,
                                          leader = leader,
                                          phonenumber = phone,
                                          description = description)
        return JsonResponse({'status': 10021, 'messages':"The product is created successful!!!"})

@csrf_exempt
def getinfo_from_product(request):
    context = {'status': 200}
    try:
        product_info = models.ProductInfo.objects.all()
    except:
        product_info = None
    if product_info == None:
        return JsonResponse({'status': 10041, 'message': 'There are no infomations'})
    data = []
    if product_info:
        for i in product_info:
            product_info_array = {}
            product_info_array['name'] = i.name
            product_info_array['leader'] = i.leader
            product_info_array['phonenumber'] = i.phonenumber
            product_info_array['description'] = i.description
            data.append(product_info_array)
        context.update({'data': data})
        return HttpResponse(json.dumps(context), content_type="application/json")

@csrf_exempt
def add_projectinfo(request):
    postbody = request.body
    json_result = json.loads(postbody)
    name = json_result["name"]
    #belongproduct = json_result["belongproduct"]
    belongproduct = json_result["value5"]
    leader = json_result["leader"]
    phone = json_result["phone_number"]
    #run = json_result["run_server"]
    run = json_result["value7"]
    description = json_result["description"]
    try:
        project = models.ProjectInfo.objects.get(name=name)
    except:
        project = None
    if project is not None:
        return JsonResponse({'status': 10051, 'messages':"The project is already exist."})
    else:
        models.ProjectInfo.objects.create(name = name,
                                          belongproduct = belongproduct,
                                          leader = leader,
                                          phonenumber = phone,
                                          server = run,
                                          description = description)
        return JsonResponse({'status': 10061, 'messages':"The project is created successful!!!"})

@csrf_exempt
def getinfo_from_project(request):
    context = {'status': 200}
    try:
        project_info = models.ProjectInfo.objects.all()
    except:
        project_info = None
    if project_info == None:
        return JsonResponse({'status': 10052, 'message': 'There are no infomations'})
    data = []
    if project_info:
        for i in project_info:
            project_info_array = {}
            project_info_array['name'] = i.name
            project_info_array['belongproduct'] = i.belongproduct
            project_info_array['leader'] = i.leader
            project_info_array['phonenumber'] = i.phonenumber
            project_info_array['runserver'] = i.server
            project_info_array['description'] = i.description
            data.append(project_info_array)
        context.update({'data': data})
        return HttpResponse(json.dumps(context), content_type="application/json")



