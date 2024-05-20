import psutil
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

from course_aws.utils import load_cpu


def index(request):
    return render(request, 'monitor.html', context={
        'instance_id': settings.INSTANCE_ID,
        "a_zone": settings.A_ZONE,
    })


def cpu_load(request):
    load_cpu()
    return JsonResponse({"result": "ok"})


def cpu_usage(request):
    return JsonResponse({"cpu": psutil.cpu_percent()})
