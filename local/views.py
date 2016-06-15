# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Action, User, Url
from django.views.decorators.csrf import csrf_exempt
import time
import datetime
import json


@csrf_exempt
def register(request):
    response = {'status': "", 'msg': ""}

    data = request.POST
    try:
        account = data['account']
        password = data['password']
        email = data['email']
    except Exception:
        response['status'] = 2
        response['msg'] = "no enough argument"
        return HttpResponse(json.dumps(response))

    is_exist = User.objects.filter(account=account).count()  # 判断账户是否已经存在
    if is_exist:
        response['status'] = 1
        response['msg'] = "account exists"
        return HttpResponse(json.dumps(response))
    else:
        User(account=account, password=password, email=email).save()
        response['status'] = 0
        response['msg'] = 'success'
        return HttpResponse(json.dumps(response))


@csrf_exempt
def login(requset):
    response = {'status': '', 'msg': ''}

    data = requset.POST
    try:  # 参数时候正确
        account = data['account']
        password = data['password']
    except Exception:
        response['status'] = 3
        response['msg'] = "no enough argument"
        return HttpResponse(json.dumps(response))

    is_exist = User.objects.filter(account=account).count()
    if is_exist:  # 账户是否存在
        user = User.objects.get(account=account)
        if password == user.password:  # 密码是否正确
            response['status'] = 0
            response['msg'] = 'success'
            return HttpResponse(json.dumps(response))
        else:
            response['status'] = 1
            response['msg'] = "password is not correct"
            return HttpResponse(json.dumps(response))
    else:
        response['status'] = 2
        response['msg'] = 'no this account'
        return HttpResponse(json.dumps(response))


@csrf_exempt
def add_url(request):
    response = {'status': '', 'msg': ''}

    data = request.POST
    try:  # 参数是否正确
        account = data['account']
        url_name = data['url_name']
        url_id = data['url_id']
        url_address = data['url_address']
        url_rank = data['url_rank']
    except Exception:
        response['status'] = 3
        response['msg'] = "no enough argument"
        return HttpResponse(json.dumps(response))

    is_exist = Url.objects.filter(url_id=url_id).count()  # 是否已经存在于Url表中
    if is_exist:  # 存在则只需要向User表对应的account中添加
        user = User.objects.get(account=account)
        if url_address in user.url:  # 判断网址是否已经在用户的url中
            user.save()
            response['status'] = 2
            response['msg'] = "url in User and Url so don't need to add"
            return HttpResponse(json.dumps(response))
        if user.url == "":
            user.url = url_address
        else:
            user.url = url_address + "-" + user.url
        user.save()
        response['status'] = 1
        response['msg'] = "add url to User but exist in Url"
        return HttpResponse(json.dumps(response))
    else:  # 如果Url表中都不存在 则需向Url和User中添加信息
        Url(url_name=url_name, url_address=url_address, url_id=url_id, url_rank=url_rank).save()
        user = User.objects.get(account=account)
        if user.url == "":
            user.url = url_address
        else:
            user.url = url_address + "-" + user.url
        user.save()
        response['status'] = 0
        response['msg'] = 'add url to Url and User'
        return HttpResponse(json.dumps(response))


@csrf_exempt
def get_user_url(request):
    response = {'status': '', 'msg': '',}
    data = list()

    get_data = request.POST
    try:
        account = get_data['account']
    except Exception:
        response['status'] = 3
        response['msg'] = "no enough argument"
        return HttpResponse(json.dumps(response))

    # 获得用户所关注的url的概述 获得url所对应的id
    urls = User.objects.get(account=account).url
    if urls == "":
        response['status'] = 4
        response['msg'] = "need to add url"
        return HttpResponse(json.dumps(response))
    url_list = urls.split("-")
    url_id_list = list()
    for url in url_list:
        if url != "":
            url_id = Url.objects.get(url_address=url).url_id
            url_name = Url.objects.get(url_address=url).url_name
            data.append({'name': url_name, 'id': url_id})
            url_id_list.append(url_id)
    # 选取相关时间
    # tomorrow = int(time.mktime((datetime.date.today()+datetime.timedelta(days=1)).timetuple()))
    # today = int(time.mktime(datetime.date.today().timetuple()))
    # yesterday = int(time.mktime((datetime.date.today()+datetime.timedelta(days=-1)).timetuple()))
    # week = int(time.mktime((datetime.date.today() + datetime.timedelta(days=-7)).timetuple()))
    today = int(time.mktime(datetime.datetime(2016, 6, 7).timetuple()))
    tomorrow = int(time.mktime((datetime.datetime(2016, 6, 7) + datetime.timedelta(days=1)).timetuple()))
    yesterday = int(time.mktime((datetime.datetime(2016, 6, 7) + datetime.timedelta(days=-1)).timetuple()))
    week = list()
    week.append(today)
    for j in range(1, 8):
        week.append(int(time.mktime((datetime.datetime(2016, 6, 7) + datetime.timedelta(days=-j)).timetuple())))

    for i in range(0, len(url_id_list)):
        each_url_data = Action.objects.filter(idsite=url_id_list[i]).filter(field_date__gte=week[7]).filter(field_date__lte=tomorrow)
        today_data = each_url_data.filter(field_date__gte=today)
        data[i]['today'] = {}
        data[i]['today']['pv'] = today_data.count()
        data[i]['today']['ip'] = today_data.values('ip').distinct().count()

        data[i]['week'] = {'pv': 0, 'ip': 0}
        j = 7
        while j > 0:
            each_day_data = each_url_data.filter(field_date__gte=week[j]).filter(field_date__lte=week[j-1])
            data[i]['week']['pv'] += each_day_data.count()
            data[i]['week']['ip'] += each_day_data.values('ip').distinct().count()
            j -= 1
        # data[i]['week']['pv'] = week_data.count()
        # data[i]['week']['ip'] = week_data.values('ip').distinct().count()

        yesterday_data = each_url_data.filter(field_date__lte=today).filter(field_date__gte=yesterday)
        data[i]['yesterday'] = {}
        data[i]['yesterday']['pv'] = yesterday_data.count()
        data[i]['yesterday']['ip'] = yesterday_data.values('ip').distinct().count()

    return HttpResponse(json.dumps(data))


@csrf_exempt
def delete_user_url(request):
    response = {'status': "", 'msg': ""}

    get_data = request.POST
    try:
        account = get_data['account']
        url_id = get_data['url_id']
    except Exception:
        response['status'] = 1
        response['msg'] = "no enough argument"
        return HttpResponse(json.dumps(response))

    user_data = User.objects.get(account=account)
    url = Url.objects.get(url_id=url_id).url_address
    new_url = user_data.url.replace(url, "")
    user_data.url = new_url
    user_data.save()
    response['status'] = 0
    response['msg'] = "delete success"
    return HttpResponse(json.dumps(response))


@csrf_exempt
def get_url_detail(request):
    response = {'status': "", 'msg': ""}

    get_data = request.POST
    try:
        url_id = get_data['url_id']
    except Exception:
        response['status'] = 1
        response['msg'] = "no enough argument"
        return HttpResponse(json.dumps(response))













