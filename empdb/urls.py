from django.urls import path,include
from .views import *


urlpatterns = [
    path('',allotment,name="allotment"),
    path('plotallotment/',plotallotment,name='plotallotment'),
    path('allotmentlist/',plotlist,name='plotlist'),
]