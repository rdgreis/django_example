from django.shortcuts import render
from datetime import timedelta
import socket


def home(request):
    context = {}
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(timedelta(seconds = uptime_seconds))
    except:
        uptime_string = 'Not available!'
    context['ip'] = socket.gethostbyname(socket.gethostname())
    context['uptime'] = uptime_string
    context['hostname'] = socket.gethostname()
    return render(request, 'home.html', context)