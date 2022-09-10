from django.urls import path,include
from .views import *


urlpatterns = [
    #path('allotment/',include('empdb.urls')),
    path('',home,name="home"),
    path('allotment/',allotment,name="allotment"),
    path('allotment/plotallotment/',plotallotment,name='plotallotment'),
    path('allotment/allotmentlist/',plotlist,name='plotlist'),
    path('allotment/allotmentcancel/',plotcancel,name='plotcancel'),
    #path('allotment/',allotment,name="allotment"),
    path('receipt/',receipt,name="receipt"),
    path('charges/',charges,name="charges"),
    path('report/',report,name="report"),
    path('receipt/receiptlist/',receiptlist,name="receiptlist"),
    path('receipt/receiptcancel/',receiptcancel,name="receiptcancel"),
]