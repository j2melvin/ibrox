from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from datetime import datetime
import os
import pytz
import RPi.GPIO as GPIO
import time

CAMERA_FILE = "/home/pi/camera/current.jpg"


@method_decorator(csrf_exempt)
def index(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('trigger', '0') == '1':
            # Trigger garage door opener
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(7, GPIO.OUT)
            GPIO.output(7, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(7, GPIO.LOW)

        return render(request, 'control/success.html', context)

    return render(request, 'control/index.html', context)

def live_feed(request):
    mountain = pytz.timezone('US/Mountain')
    try:
        last_mod = datetime.utcfromtimestamp(os.path.getmtime(CAMERA_FILE)).replace(tzinfo=pytz.utc)
        context = {'last_update': str(last_mod.astimezone(mountain).strftime("%Y-%m-%d %I:%M:%S %p"))}
    except:
        context = {'last_update': "Not Available"}

    return render(request, 'control/live_feed.html', context)

