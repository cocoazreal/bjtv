from django.shortcuts import render
from django.http import HttpResponse
from .models import Action
from django.views.decorators.csrf import csrf_exempt
import time
import json


def index(request):
    date = time.time()
    data = Action.objects.values('ip').distinct().count()
    # ip = set()
    # for e in data.iterator():
    #  return HttpResponse(str(date) + ',' + str(len(ip)) + "," + str(time.time()))

    return HttpResponse(str(date) + ',' + str(data) + ',' + str(time.time()))


@csrf_exempt
def register(request):
    data = request.POST
    return HttpResponse(json.dumps(data))
