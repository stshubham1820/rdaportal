from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('',master,name="master"),
    

#Master
    path('usermaster/',usermaster,name="usermaster"),
    path('plottypemaster/',plottypemaster,name="plottypemaster"),
    path('projectmaster/',projectmaster,name="projectmaster"),
    path('categorymaster/',categorymaster,name="categorymaster"),
    path('plotflagmaster/',plotflagmaster,name="plotflagmaster"),
    path('gstmaster/',gstmaster,name="gstmaster"),
    path('areamaster/',areamaster,name="areamaster"),
    path('sectormaster/',sectormaster,name="sectormaster"),
    path('plotaddmaster/',plotaddmaster,name="plotaddmaster"),
    path('plottypemaster/edit/',plottypeedit,name="plottypeedit"),
    path('plottypemaster/del/',plottypedel,name="plottypedel"),
    path('usermaster/del/',usermasterdel,name="usermasterdel"),
    path('projectmaster/edit/',projedit,name="projedit"),
    path('projectmaster/del/',projdel,name="projdel"),
    path('plotflagmaster/edit/',plotflagedit,name="plotflagedit"),
    path('plotflagmaster/del/',plotflagdel,name="plotflagdel"),
    path('areamaster/edit/',areaedit,name="areaedit"),
    path('areamaster/del/',areadel,name="areadel"),
    path('categorymaster/edit/',categoryedit,name="categoryedit"),
    path('categorymaster/del/',categorydel,name="categorydel"),
    path('gstmaster/edit/',gstedit,name="gstedit"),
    path('gstmaster/del/',gstdel,name="gstdel"),
    path('sectormaster/edit/',sectoredit,name="sectoredit"),
    path('sectormaster/del/',sectordel,name="sectordel"),
    path('plotaddmaster/data/',allplot,name="allplot"),
]