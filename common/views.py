from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
@api_view(['Post'])
@permission_classes([IsAuthenticated])
def log(request):
    user = request.POST.get("username")
    if user.user_type == "Admin":
        url = "/employeedb/"
    elif user.user_type == "Citizen":
        url = "/citizen_portal/"
    else :
        url = "/"
    return redirect(url)


