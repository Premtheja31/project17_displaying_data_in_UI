from django.shortcuts import render
from app.models import *
# Create your views here.
def table(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'table.html',d)

def AR(request):
    LARO=AccessRecords.objects.all()
    d={'LARO':LARO}
    return render(request,'AR.html',d)

def WP(request):
    LWPO=Webpage.objects.all()
    d={'LWPO':LWPO}
    return render(request,'WP.html',d)