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

def statusId(request):
    status = createStatus()
    return JsonResponse({"id": status.id})

def decode(request, id):
    image = request.FILES.get("image")

    decoded_text = enhanced_retr(image, id)

    return JsonResponse({"Success": True, "Text": decoded_text})

def encode(request, id):
    """
    Turn on CSRF middleware in settings.py later
    """

    print(request)

    if request.method == "GET":
        return JsonResponse({"Success": False})

    text = request.POST.get("text")
    text = text.encode()
    
    txtFile = request.FILES.get("txtFile")
    if txtFile:
        text  = txtFile.read()
    
    print(text)

    image = request.FILES.get("image")

    img = enhanced_hide(image, text, id)

    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="myImg.png"'
    img.save(response, "PNG")
    return(response)


def homePage(request):
    return render(request, "steganography/index.html")
    
def hide(request):
    return render(request, "steganography/hide.html")

def statusMeter(request, id):
    progress = getProgress(id)
    return JsonResponse({"progress": progress})