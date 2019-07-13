from django.shortcuts import render
from subprocess import Popen, PIPE, STDOUT


def homepage(request):
    image_file_name = "/home/craig/Pictures/theta/2019/z1-test-image/R0010765.JPG"
    process = Popen(['exiftool', image_file_name], stdout=PIPE, stderr=STDOUT)
    output_byte = process.stdout.read()
    output_list = str(output_byte)[2:-1].strip().split('\\n')
    return render(request, 'home.html', {"output": output_list})


