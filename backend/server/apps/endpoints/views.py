from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from apps.steganography.allPixels import enhanced_hide, enhanced_retr, rgb2hex
# Create your views here.
from PIL import Image
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def decode(request):
    data = {"text": rgb2hex(20, 40, 50)}
    # return HttpResponse(data, content_type='application/json')
    return JsonResponse(data)

def encode(request):
    """
    Turn on CSRF middleware in settings.py later
    """

    if request.method == "GET":
        return JsonResponse({"Success": False})

    text = request.POST.get("text")
    image = request.FILES.get("image")

    img = enhanced_hide(image, text.encode())

    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="myImg.png"'
    img.save(response, "PNG")
    return(response)

    return JsonResponse({"Success": True})

