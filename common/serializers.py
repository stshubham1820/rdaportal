from django.urls import path, include
from .models import CustomUser
from .models import *
from rest_framework import serializers

class userser(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"