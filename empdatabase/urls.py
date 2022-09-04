from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('master/',master,name="master"),
    path('allotment/',include('empdb.urls')),
    #path('allotment/',allotment,name="allotment"),
    path('receipt/',receipt,name="receipt"),
    path('charges/',charges,name="charges"),
    path('report/',report,name="report"),

#Master
    path('master/usermaster/',usermaster,name="usermaster"),
    path('master/plottypemaster/',plottypemaster,name="plottypemaster"),
    path('master/projectmaster/',projectmaster,name="projectmaster"),
    path('master/categorymaster/',categorymaster,name="categorymaster"),
    path('master/plotflagmaster/',plotflagmaster,name="plotflagmaster"),
    path('master/gstmaster/',gstmaster,name="gstmaster"),
    path('master/areamaster/',areamaster,name="areamaster"),
    path('master/sectormaster/',sectormaster,name="sectormaster"),
    path('master/plotaddmaster/',plotaddmaster,name="plotaddmaster"),
    path('master/plottypemaster/edit/',plottypeedit,name="plottypeedit"),
    path('master/plottypemaster/del/',plottypedel,name="plottypedel"),
    path('master/usermaster/del/',usermasterdel,name="usermasterdel"),
    path('master/projectmaster/edit/',projedit,name="projedit"),
    path('master/projectmaster/del/',projdel,name="projdel"),
    path('master/plotflagmaster/edit/',plotflagedit,name="plotflagedit"),
    path('master/plotflagmaster/del/',plotflagdel,name="plotflagdel"),
    path('master/areamaster/edit/',areaedit,name="areaedit"),
    path('master/areamaster/del/',areadel,name="areadel"),
    path('master/categorymaster/edit/',categoryedit,name="categoryedit"),
    path('master/categorymaster/del/',categorydel,name="categorydel"),
    path('master/gstmaster/edit/',gstedit,name="gstedit"),
    path('master/gstmaster/del/',gstdel,name="gstdel"),
    path('master/sectormaster/edit/',sectoredit,name="sectoredit"),
    path('master/sectormaster/del/',sectordel,name="sectordel"),
    path('master/plotaddmaster/data/',allplot,name="allplot"),
]