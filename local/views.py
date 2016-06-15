# coding:utf-8
from __future__ import division
from django.http import HttpResponse
from .models import Action, User, Url, Daydata
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
    response = {'status': '', 'msg': ''}
    data = list()

    get_data = request.POST
    try:
        account = get_data['account']
    except Exception:
        response['status'] = 1
        response['msg'] = "no enough argument"
        return HttpResponse(json.dumps(response))

    # 获得用户所关注的url的概述 获得url所对应的id
    urls = User.objects.get(account=account).url
    if urls == "":
        response['status'] = 2
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

    # timestamp = time.time()
    timestamp = int(time.mktime(time.strptime("2016-06-08 00:00:00", '%Y-%m-%d %H:%M:%S')))
    timestruct = time.localtime(timestamp)
    year = time.strftime("%Y", timestruct)
    month = time.strftime("%m", timestruct)
    week = time.strftime("%W", timestruct)
    day = time.strftime("%d", timestruct)
    # 昨天的数据要单独处理方式出现跨年 跨月而不正常的现象
    yesterday_timestamp = int(time.mktime((datetime.datetime(2016, 6, 8) + datetime.timedelta(days=-1)).timetuple()))
    yesterday_timestruct = time.localtime(yesterday_timestamp)
    yesterday_year = time.strftime("%Y", yesterday_timestruct)
    yesterday_month = time.strftime("%m", yesterday_timestruct)
    yesterday_day = time.strftime("%d", yesterday_timestruct)

    for i in range(0, len(url_id_list)):
        week_data = Daydata.objects.filter(idsite=url_id_list[i]).filter(year=year).filter(week=week)
        data[i]['week'] = {'ip': 0, 'pv': 0}
        for each in week_data:
            data[i]['week']['ip'] += each.ip
            data[i]['week']['pv'] += each.pv
        today_data = Daydata.objects.filter(idsite=url_id_list[i]).filter(year=year).filter(month=month).filter(day=day)
        data[i]['today'] = {'ip': 0, 'pv': 0}
        for each in today_data:
            data[i]['today']['ip'] += each.ip
            data[i]['today']['pv'] += each.pv
        yesterday_data = Daydata.objects.filter(idsite=url_id_list[i]).filter(year=yesterday_year).\
            filter(month=yesterday_month).filter(day=yesterday_day)
        data[i]['yesterday'] = {'ip': 0, 'pv': 0}
        for each in yesterday_data:
            data[i]['yesterday']['ip'] += each.ip
            data[i]['yesterday']['pv'] += each.pv

    response['status'] = 0
    response['msg'] = 'ok'
    response['data'] = data
    return HttpResponse(json.dumps(response))


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

    url_data = Url.objects.get(url_id=url_id)
    response['name'] = url_data.url_name
    response['address'] = url_data.url_address

    # timestamp = time.time()
    timestamp = int(time.mktime(time.strptime("2016-06-08 00:00:00", '%Y-%m-%d %H:%M:%S')))
    timestruct = time.localtime(timestamp)
    year = time.strftime("%Y", timestruct)
    month = time.strftime("%m", timestruct)
    week = time.strftime("%W", timestruct)
    day = time.strftime("%d", timestruct)
    # 昨天的数据要单独处理方式出现跨年 跨月而不正常的现象
    yesterday_timestamp = int(time.mktime((datetime.datetime(2016, 6, 8) + datetime.timedelta(days=-1)).timetuple()))
    yesterday_timestruct = time.localtime(yesterday_timestamp)
    yesterday_year = time.strftime("%Y", yesterday_timestruct)
    yesterday_month = time.strftime("%m", yesterday_timestruct)
    yesterday_day = time.strftime("%d", yesterday_timestruct)

    data = {}
    # 总的
    all_data = Daydata.objects.filter(idsite=url_id)
    data['all'] = {'ip': 0, 'pv': 0, 'uv': 0}
    for each in all_data:
        data['all']['ip'] += each.ip
        data['all']['pv'] += each.pv
        data['all']['uv'] += each.uv
    # 今天
    today_data = Daydata.objects.filter(idsite=url_id).filter(year=year).filter(month=month).filter(day=day)
    data['today'] = {'ip': 0, 'pv': 0, 'uv': 0}
    for each in today_data:
        data['today']['ip'] += each.ip
        data['today']['pv'] += each.pv
        data['today']['uv'] += each.uv
    # 昨天
    yesterday_data = Daydata.objects.filter(idsite=url_id).filter(year=yesterday_year).filter(
        month=yesterday_month).filter(day=yesterday_day)
    data['yesterday'] = {'ip': 0, 'pv': 0, 'uv': 0}
    for each in yesterday_data:
        data['yesterday']['ip'] += each.ip
        data['yesterday']['pv'] += each.pv
        data['yesterday']['uv'] += each.uv
    # 今年
    year_data = Daydata.objects.filter(idsite=url_id).filter(year=year)
    data['year'] = {'ip': 0, 'pv': 0, 'uv': 0}
    for each in year_data:
        data['year']['ip'] += each.ip
        data['year']['pv'] += each.pv
        data['year']['uv'] += each.uv
    # 本月
    nonth_data = Daydata.objects.filter(idsite=url_id).filter(year=year).filter(month=month)
    data['month'] = {'ip': 0, 'pv': 0, 'uv': 0}
    for each in nonth_data:
        data['month']['ip'] += each.ip
        data['month']['pv'] += each.pv
        data['month']['uv'] += each.uv
    # 总天数
    all_days = Daydata.objects.values('year', 'month', 'day').distinct().count()
    # 平均每天
    data['ave_day'] = {'ip': 0, 'pv': 0, 'uv': 0}
    data['ave_day']['ip'] = int(data['all']['ip'] / all_days)
    data['ave_day']['pv'] = int(data['all']['pv'] / all_days)
    data['ave_day']['uv'] = int(data['all']['uv'] / all_days)
    # 历史最高
    days = Daydata.objects.values('year', 'month', 'day').distinct()
    data['max_ip'] = {'ip': 0, 'date': ""}
    data['max_uv'] = {'uv': 0, 'date': ""}
    data['max_pv'] = {'pv': 0, 'date': ""}
    data['max_avg_ip'] = {'avg_ip': 0, 'date': ""}
    for each_day in days:
        each_day_ip = 0
        each_day_pv = 0
        each_day_uv = 0

        max_year = each_day['year']
        max_month = each_day['month']
        max_day = each_day['day']
        max_data = Daydata.objects.filter(year=max_year).filter(month=max_month).filter(day=max_day)
        for each_data in max_data:
            each_day_ip += each_data.ip
            each_day_pv += each_data.pv
            each_day_uv += each_data.uv
        each_day_avg_ip = ("%.2f" % (each_day_pv / each_day_ip))

        if each_day_ip >= data['max_ip']['ip']:
            data['max_ip']['ip'] = each_day_ip
            data['max_ip']['date'] = str(max_year) + "." + str(max_month) + "." + str(max_day)
        if each_day_pv >= data['max_pv']['pv']:
            data['max_pv']['pv'] = each_day_pv
            data['max_pv']['date'] = str(max_year) + "." + str(max_month) + "." + str(max_day)
        if each_day_uv >= data['max_uv']['uv']:
            data['max_uv']['uv'] = each_day_uv
            data['max_uv']['date'] = str(max_year) + "." + str(max_month) + "." + str(max_day)
        if each_day_avg_ip >= data['max_avg_ip']['avg_ip']:
            data['max_avg_ip']['avg_ip'] = each_day_avg_ip
            data['max_avg_ip']['date'] = str(max_year) + "." + str(max_month) + "." + str(max_day)

    response['status'] = 0
    response['msg'] = 'ok'
    response['data'] = data
    return HttpResponse(json.dumps(response))

















