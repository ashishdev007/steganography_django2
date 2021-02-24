from apps.steganography.models import StatusTracker
from django.core.exceptions import ObjectDoesNotExist


def createStatus():
    status = StatusTracker(progress=0)
    status.save()

    return status

def getProgress(id):
    try:
        status = StatusTracker.objects.get(id=id)
        return status.progress
    except(ObjectDoesNotExist):
        return -1

def setProgress(id, progress):
    try:
        status = StatusTracker.objects.get(id=id)
        status.update(progress=progress)
    except(ObjectDoesNotExist):
        pass

def deleteStatus(id):
    try:
        status = StatusTracker.objects.get(id=id)
        status.delete()
    except(ObjectDoesNotExist):
        pass

def temp():
    allItems = StatusTracker.objects.all()
    answer = []
    for item in allItems:
        answer.append(item.id)
    
    return answer