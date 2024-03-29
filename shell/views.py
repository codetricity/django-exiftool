from django.shortcuts import render
from subprocess import Popen, PIPE, STDOUT
import requests
import json
import os


THETA_IP = '192.168.1.1'
PROJECT_MEDIA_DIR = os.getcwd() + "/media/"


def homepage(request):
    return render(request, 'home.html')


def exif(request):
    # pass in file name after upload for production
    image_file_name = f"{PROJECT_MEDIA_DIR}/osaka-night.jpg"
    process = Popen(['exiftool', image_file_name], stdout=PIPE, stderr=STDOUT)
    output_byte = process.stdout.read()
    output_list = str(output_byte)[2:-1].strip().split('\\n')
    return render(request, 'exif.html', {"output": output_list, "filename": image_file_name.split('/')[-1]})


def theta(request):
    url = f"http://{THETA_IP}/osc/info"
    # URL below is for testing only
    # url = "https://httpbin.org/get"
    r = requests.request('GET', url)
    data = r.json()
    print(data)

    return render(request, 'commandhome.html', {'data': data})


def watermark(request):
    # pass in file name after upload for production
    image_file_name = f"{PROJECT_MEDIA_DIR}/toyo-hardrock.jpg"
    logo_file_name = f"{PROJECT_MEDIA_DIR}/theta_logo.png"
    output_file = f"{PROJECT_MEDIA_DIR}/new-image.jpg"
    # composite is part of imagemagick package
    Popen(['composite', '-geometry', '+3000+1600', logo_file_name,
        image_file_name, output_file], stdout=PIPE, stderr=STDOUT)

    return render(request, 'watermark.html', {"output": output_file.split('/')[-1]})

