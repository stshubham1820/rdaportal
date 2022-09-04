from django.shortcuts import render

# Create your views here.
def allotment(request):
    return render(request,"empdatabase/allotment.html",{"obj2":"Style = color:#FFF5F9;",'newclr2':'newclr',"page":"Allotment","css1":"Style = display:none;"})


def plotallotment(request):
    return render(request,"empdatabase/allotment/plotallotment.html",{"obj2":"Style = color:#FFF5F9;",'newclr2':'newclr',"page":"Allotment","css1":"Style = display:none;","obj13":"Style = display:none;"})