from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def decode(request):
    data = {"text": "My Text!!"}
    # return HttpResponse(data, content_type='application/json')
    return JsonResponse(data)