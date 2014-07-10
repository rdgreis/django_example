import socket
import hashlib
from random import choice
from string import uppercase
from django.shortcuts import render
from datetime import timedelta
from pif import get_public_ip
from datetime import datetime,timedelta


def generate_load(size=10):
    text = []
    for i in range(size):
        text.append(choice(uppercase))
    hash = hashlib.md5()
    hash.update(''.join(text))
    hash.digest()

def home(request):
    context = {}
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(timedelta(seconds = uptime_seconds))
    except:
        uptime_string = 'Not available!'

    if request.GET:
        minutes = int(request.GET.get('minutes'))
        now = datetime.now()
        while (datetime.now()-now).seconds <= (minutes*60):
            generate_load(30)

    context['ip'] = get_public_ip()
    context['uptime'] = uptime_string
    context['hostname'] = socket.gethostname()
    return render(request, 'home.html', context)