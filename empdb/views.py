from django.shortcuts import render
from empdatabase.models import *

# Create your views here.
def allotment(request):
    return render(request,"empdatabase/allotment.html",{"obj2":"Style = color:#FFF5F9;",'newclr2':'newclr',"page":"Allotment","css1":"Style = display:none;"})


def plotallotment(request):
    return render(request,"empdatabase/allotment/allotment.html",{"obj2":"Style = color:#FFF5F9;",'newclr2':'newclr',"page":"Allotment","subpage":"Plot Allotment","obj13":"Style = display:none;"})

def plotlist(request):
    pro = ProjectName.objects.all().order_by('Project_Name')
    return render(request,"empdatabase/allotment/list.html",{"obj2":"Style = color:#FFF5F9;",'newclr2':'newclr',"page":"Allotment","subpage":"Allotment List","obj13":"Style = display:none;","pro_data":pro})