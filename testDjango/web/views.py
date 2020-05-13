from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
import json
# Create your views here.

username = 0


def LoginPost(request):

    if request.method == "POST":
        username = request.POST.get('username')
        print(username)
        return HttpResponse(username)
    else:
        return render_to_response('login.html')


def LoginGet(request):
    if request.method == "GET":
        username = request.GET.get('username')
        password = request.GET.get('pass')
        data = request.GET.get('data')

        result ={
                'username': username,
                'password': password,
                'data': data

        }

        '将字典序列化'
        result = json.dumps(result)


        return HttpResponse(result, content_type = 'application/json;charset=UTF-8')
    else:
        return render_to_response('login.html')
