# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    message=""
    if request.method == 'POST':
        # hit AWS API w/ requests
        label_img = request.POST.get("label_img", "")
        screenshot_img = request.POST.get("screenshot_img_input", "")
        message = 'Image invalid. Please upload an image of a nutrition label.'
        print('screenshot_img')
        print(screenshot_img)
        print('label_img')
        print(label_img)
        if screenshot_img:
            payload = {'label_img': label_img, 'user': request.user}
            # response = requests.post('https://httpbin.org/get', params=payload)
            # check response
            message = 'Image upload successful.'
        elif label_img:
            payload = {'label_img': label_img, 'user': request.user}
            # response = requests.post('https://httpbin.org/get', params=payload)
            # check response
            message = 'Image upload successful.'
        else:
            return render(request, 'general/index.html', {'message':message})
        return JsonResponse({'message': message})
    return render(request, 'general/index.html', {'message': message})