from django.shortcuts import render
from empdatabase.models import *

# Create your views here.
def home(request):
    return render(request,"empdatabase/dashboard.html",{"obj":"Style = color:#FFF5F9;",'newclr':'newclr',"css":"Style = display:none;","css1":"Style = display:none;"})



def receipt(request):
    return render(request,"empdatabase/receipt.html",{"obj3":"Style = color:#FFF5F9;",'newclr3':'newclr',"page":"Receipt","css1":"Style = display:none;"})


def charges(request):
    return render(request,"empdatabase/charges.html",{"obj4":"Style = color:#FFF5F9;",'newclr4':'newclr',"page":"Charges","css1":"Style = display:none;"})

def report(request):
    return render(request,"empdatabase/report.html",{"obj5":"Style = color:#FFF5F9;",'newclr5':'newclr',"page":"Report","css1":"Style = display:none;"})



def allotment(request):
    return render(request,"empdatabase/allotment.html",{"obj2":"Style = color:#FFF5F9;",'newclr2':'newclr',"page":"Allotment","css1":"Style = display:none;"})


def plotallotment(request):
    return render(request,"empdatabase/allotment/allotment.html",{"obj2":"Style = color:#FFF5F9;",'newclr2':'newclr',"page":"Allotment","subpage":"Plot Allotment","obj13":"Style = display:none;"})


def plotcancel(request):
    return render(request,"empdatabase/allotment/allotmentcancel.html",{"obj2":"Style = color:#FFF5F9;",'newclr2':'newclr',"page":"Allotment","subpage":"Plot Allotment","obj13":"Style = display:none;"})


def plotlist(request):
    pro = ProjectName.objects.all().order_by('Project_Name')
    return render(request,"empdatabase/allotment/list.html",{"obj2":"Style = color:#FFF5F9;",'newclr2':'newclr',"page":"Allotment","subpage":"Allotment List","obj13":"Style = display:none;","pro_data":pro})


def receiptlist(request):
    pro = ProjectName.objects.all().order_by('Project_Name')
    return render(request,"empdatabase/receipt/list.html",{"obj3":"Style = color:#FFF5F9;",'newclr3':'newclr',"page":"Allotment","subpage":"Allotment List","obj13":"Style = display:none;","pro_data":pro})


def receiptcancel(request):
    return render(request,"empdatabase/receipt/listcan.html",{"obj3":"Style = color:#FFF5F9;",'newclr3':'newclr',"page":"Allotment","subpage":"Allotment List","obj13":"Style = display:none;"})


def editpassw(request):
    return render(request,"empdatabase/editpassw.html",{"obj":"Style = color:#FFF5F9;",'newclr':'newclr',"css":"Style = display:none;","subpage":"Edit Password","obj13":"Style = display:none;"})


def editprofile(request):
    return render(request,"empdatabase/profile.html",{"obj":"Style = color:#FFF5F9;",'newclr':'newclr',"css":"Style = display:none;","subpage":"Edit Profile","obj13":"Style = display:none;"})

def sendreport(request):
    return render(request,"empdatabase/sendreport.html",{"obj":"Style = color:#FFF5F9;",'newclr':'newclr',"css":"Style = display:none;","subpage":"Send Report","obj13":"Style = display:none;"})