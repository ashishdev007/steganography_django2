from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from apps.steganography.allPixels import enhanced_hide, enhanced_retr, rgb2hex
from apps.steganography.models import StatusTracker
from apps.steganography.utils.status import createStatus, getProgress, deleteStatus, temp
# Create your views here.
from PIL import Image
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def decode(request):
    image = request.FILES.get("image")

    decoded_text = enhanced_retr(image)

    return JsonResponse({"Success": True, "Text": decoded_text})

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

def interface(request):
    return render(request, "steganography/index.html")

def statusMeter(request, id):
    progress = getProgress(id)
    return JsonResponse({"progress": progress})