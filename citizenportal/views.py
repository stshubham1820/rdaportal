from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from common.models import *
from .models import *
# Create your views here.

def home(request):
    return render(request,'build/index.html')

@api_view(['Post'])
def register(request):
    try :
        username = request.data["username"]
        password = request.data["password"]
        first = request.data["first"] if request.POST.get("first") else ""
        mid = request.data["mid"] if request.POST.get("mid") else ""
        last = request.data["last"] if request.POST.get("last") else ""
        ews = request.data["ews"] if request.POST.get("ews") else ""
        phone = request.data["phone_no"] if request.POST.get("phone_no") else 123
        aadhar = request.data["aadhar_no"] if request.POST.get("aadhar_no") else ""
        user = CustomUser.objects.create(username=username,password=password)
        user.save()
        citi = Citizen_model.objects.create(username=user,first_name=first,middle_name=mid,last_name=last,
                Ews=ews,mobile_number=phone,aadhar_number=aadhar)
        citi.save()
        return Response(status=status.HTTP_201_CREATED)
    except :
        return Response(status=request.status)