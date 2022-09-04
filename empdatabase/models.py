from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.

class MasterUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="User Name")
    fullname = models.CharField(max_length=100,null=True,blank=True,verbose_name="Full Name")
    user_level = models.CharField(max_length=100,null=False,blank=False,verbose_name="User Level")
    mobile = models.CharField(max_length=14,unique=True,null=False,blank=False,verbose_name="Mobile Number")
    user_key = models.CharField(max_length=100,null=False,blank=False,verbose_name="User Key")
    user_lock = models.BooleanField(verbose_name="User Lock",default=False)

class Plottype(models.Model):
    S_no =  models.CharField(max_length=100,unique=True,null=True,blank=True)
    Plottype = models.CharField(unique=True,max_length=100,null=False,blank=False,verbose_name="Plot Type")

class ProjectName(models.Model):
    S_no =  models.CharField(max_length=100,unique=True,null=True,blank=True)
    Project_Name = models.CharField(unique=True,max_length=100,null=False,blank=False,verbose_name="Project Name")

class PlotName(models.Model):
    S_no =  models.CharField(max_length=100,unique=True,null=True,blank=True)
    Plot_Name = models.CharField(unique=True,max_length=100,null=False,blank=False,verbose_name="Plot Name")

class CategoryName(models.Model):
    S_no =  models.CharField(max_length=100,unique=True,null=True,blank=True)
    Category_Name = models.CharField(unique=True,max_length=100,null=False,blank=False,verbose_name="Category Name")

class AreaName(models.Model):
    S_no =  models.CharField(max_length=100,unique=True,null=True,blank=True)
    Area_Name = models.CharField(unique=True,max_length=100,null=False,blank=False,verbose_name="Area Name")

class PlotFlag(models.Model):
    S_no =  models.CharField(max_length=100,unique=True,null=True,blank=True)
    Plot_Flag_Name = models.CharField(unique=True,max_length=100,null=False,blank=False,verbose_name="Plot Flag Name")

class SectorName(models.Model):
    S_no =  models.CharField(max_length=100,unique=True,null=True,blank=True)
    ProjectName = models.ForeignKey(ProjectName,on_delete=models.CASCADE,verbose_name="Project Name")
    Sector_Name = models.CharField(max_length=100,null=False,blank=False,verbose_name="Sector Name")


class GSTMaster(models.Model):
    S_no =  models.CharField(max_length=100,unique=True,null=True,blank=True)
    Head = models.CharField(unique=True,max_length=100,null=False,blank=False,verbose_name="Head")
    HSN_SAC = models.CharField(max_length=100,null=False,blank=False,verbose_name="HSN SAC")
    gst = models.BooleanField(verbose_name="GST Applicable",default=False)


class PlotMaster(models.Model):
    S_no =  models.CharField(max_length=100,unique=True,null=True,blank=True)
    Project = models.OneToOneField(ProjectName,on_delete=models.CASCADE,verbose_name="Project")
    Sector = models.OneToOneField(SectorName,on_delete=models.CASCADE,verbose_name="Sector")
    Plot_no = models.IntegerField(null=False,blank=False,verbose_name="Plot Number")
    Plot_size = models.FloatField(null=False,blank=False,verbose_name="Plot Size")
    Extra_Land = models.CharField(max_length=100,null=True,blank=True,verbose_name="Extra Land")
    Plot_type = models.OneToOneField(Plottype,on_delete=models.CASCADE,verbose_name="Plot Type")
    Plot_Category = models.OneToOneField(CategoryName,on_delete=models.CASCADE,verbose_name="Plot Category")
    Plot_Area = models.OneToOneField(AreaName,on_delete=models.CASCADE,verbose_name="Plot Area")
    Type = models.CharField(max_length=100,null=True,blank=True,verbose_name="Type")
    Tag = models.CharField(max_length=100,null=True,blank=True,verbose_name="Tag")
    Flag = models.OneToOneField(PlotFlag,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Plot Flag")

