from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
import datetime
from .manager import *
# Create your models here.

class CustomUser(AbstractBaseUser):
    User_Choices = (
        ("Employee","Employee"),
        ("Admin","Admin"),
        ("Citizen","Citizen")
    )
    id = models.AutoField(primary_key=True,unique=True)
    username = models.CharField(unique=True,max_length=50, verbose_name="Username")
    email = models.CharField(max_length=50, verbose_name="Email Address")
    first_name = models.CharField(max_length=50, verbose_name="First Name ")
    last_name = models.CharField(max_length=50 , verbose_name="Last Name ")
    date_joined = models.DateTimeField(default=datetime.datetime.now)
    phone_number = models.PositiveBigIntegerField(null=True, verbose_name="Phone Number * ")
    age = models.PositiveIntegerField(null=True, verbose_name="Age ")
    gender = models.CharField(max_length=30, null=True, verbose_name="Gender ")
    address = models.CharField(max_length=150 , null=True, verbose_name="Address ")
    user_type = models.CharField(max_length = 20,choices = User_Choices,default = "Citizen", verbose_name="User Type")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_superclinic = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.username


class ApiSetup(models.Model):
    x_apikey = models.CharField(max_length=100,null=True,blank=True,verbose_name="Api Key")
    client_Id = models.CharField(max_length=100,null=True,blank=True,verbose_name="Client Id")
    client_token = models.CharField(max_length=100,null=True,blank=True,verbose_name="Client Token")
    def __str__(self):
        return self.client_Id

