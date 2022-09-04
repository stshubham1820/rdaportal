from http.client import HTTPResponse
from sqlite3 import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def check(data):
    if data == None or data == "":
        pass
    else :
        return data


def home(request):
    return render(request,"empdatabase/dashboard.html",{"obj":"Style = color:#FFF5F9;",'newclr':'newclr',"css":"Style = display:none;","css1":"Style = display:none;"})


def master(request):
    return render(request,"empdatabase/master.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","css1":"Style = display:none;"})


def receipt(request):
    return render(request,"empdatabase/receipt.html",{"obj3":"Style = color:#FFF5F9;",'newclr3':'newclr',"page":"Receipt","css1":"Style = display:none;"})


def charges(request):
    return render(request,"empdatabase/charges.html",{"obj4":"Style = color:#FFF5F9;",'newclr4':'newclr',"page":"Charges","css1":"Style = display:none;"})

def report(request):
    return render(request,"empdatabase/report.html",{"obj5":"Style = color:#FFF5F9;",'newclr5':'newclr',"page":"Report","css1":"Style = display:none;"})

###Master####

def usermaster(request):
    userdata = MasterUser.objects.all().order_by('fullname')
    if request.POST :
        try : 
            username = request.POST.get("username")
            userkey = request.POST.get("userkey")
            userpassword = request.POST.get("user_password")
            userlevel = request.POST.get("user_level")
            userfullname = request.POST.get("name")
            usermobile = request.POST.get("mobile")
            user_email_id = request.POST.get("email")
            userlock = request.POST.get("lock")
            if userlock == "Yes" :
                userlock = True
            else :
                userlock = False
            user = User.objects.create(username=username,password=userpassword,email=user_email_id)
            user.save()
            user = User.objects.get(username=username)
            mast = MasterUser.objects.create(user=user,fullname=userfullname,user_level=userlevel,mobile=usermobile,user_key=userkey,user_lock=userlock)
            mast.save()
            userdata = MasterUser.objects.all().order_by('fullname')
            return render(request,"empdatabase/master/usermaster.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"User Master","message":"User has been Created Sucessfully","userdata":userdata})
        except IntegrityError :
            return render(request,"empdatabase/master/usermaster.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"User Master","message":"User is Already Here","userdata":userdata})
        except Exception as err:
            print(err)
    return render(request,"empdatabase/master/usermaster.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"User Master","obj13":"Style = display:none;","userdata":userdata})

def plottypemaster(request):
    plot_data = Plottype.objects.all().order_by('S_no')
    if request.POST:
        try :
            plot_type = request.POST.get("type_name")
            plottype = Plottype.objects.create(Plottype=plot_type)
            plottype.save()
            plot_ = Plottype.objects.get(Plottype=plot_type)
            plot_.S_no = len(plot_data)
            plot_.save()
            plot_data = Plottype.objects.all().order_by('S_no')
            return render(request,"empdatabase/master/ploatmaster.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Plot Type Master","message":"Plot Type has been saved Sucessfully","plotdata":plot_data})
        except IntegrityError :
            return render(request,"empdatabase/master/ploatmaster.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Plot Type Master","message":"Entered Plot Type is already in the Database","plotdata":plot_data})
        except Exception as err:
            print(err)
    return render(request,"empdatabase/master/ploatmaster.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Plot Type Master","obj13":"Style = display:none;","plotdata":plot_data})

def projectmaster(request):
    pro_data = ProjectName.objects.all().order_by('S_no')
    if request.POST:
        try :
            pro_type = request.POST.get("type_name")
            protype = ProjectName.objects.create(Project_Name=pro_type)
            protype.save()
            proj_ = ProjectName.objects.get(Project_Name=pro_type)
            proj_.S_no = len(pro_data)
            proj_.save()
            pro_data = ProjectName.objects.all().order_by('S_no')
            return render(request,"empdatabase/master/project.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Project Master","message":"Project Name has been Added Sucessfully","pro_data":pro_data})
        except IntegrityError :
            return render(request,"empdatabase/master/project.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Project Master","message":" This Project Name is already in our Database","pro_data":pro_data})
        except Exception as err:
            print(err)
    return render(request,"empdatabase/master/project.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Project Master","obj13":"Style = display:none;","pro_data":pro_data})

def categorymaster(request):
    cat_data = CategoryName.objects.all().order_by('S_no')
    if request.POST:
        try :
            catd_ = request.POST.get("type_name")
            cat = CategoryName.objects.create(Category_Name=catd_)
            cat.save()
            cat_ = CategoryName.objects.get(Category_Name=catd_)
            cat_.S_no = len(cat_data)
            cat_.save()
            cat_data = CategoryName.objects.all().order_by('S_no')
            return render(request,"empdatabase/master/category.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Category Master","message":"Category has been sucessfully added","cat_data":cat_data})
        except IntegrityError :
            return render(request,"empdatabase/master/category.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Category Master","message":"This category is already there in our Database","cat_data":cat_data})
        except Exception as err:
            print(err)
    return render(request,"empdatabase/master/category.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Category Master","obj13":"Style = display:none;","cat_data":cat_data})

def plotflagmaster(request):
    flg_data = PlotFlag.objects.all().order_by('S_no')
    if request.POST:
        try :
            flag_d = request.POST.get("type_name")
            flag = PlotFlag.objects.create(Plot_Flag_Name=flag_d)
            flag.save()
            flag_ = PlotFlag.objects.get(Plot_Flag_Name=flag_d)
            flag_.S_no = len(flg_data)
            flag_.save()
            flg_data = PlotFlag.objects.all().order_by('S_no')
            render(request,"empdatabase/master/plotflag.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Plot Flag Master","message": "Plot Flag has been sucessfully Uploaded","flg_data":flg_data})
        except IntegrityError :
            render(request,"empdatabase/master/plotflag.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Plot Flag Master","message": "This Plot flag is already there in our Database","flg_data":flg_data})
        except Exception as err:
            print(err)
    return render(request,"empdatabase/master/plotflag.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Plot Flag Master","obj13":"Style = display:none;","flg_data":flg_data})

def areamaster(request):
    area_data = AreaName.objects.all().order_by('S_no')
    if request.POST:
        try :
            area_d = request.POST.get("type_name")
            area = AreaName.objects.create(Area_Name=area_d)
            area.save()
            area_ = AreaName.objects.get(Area_Name=area_d)
            area_.S_no = len(area_data)
            area_.save()
            area_data = AreaName.objects.all().order_by('S_no')
            return render(request,"empdatabase/master/area.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Area Master","message":"Area name has been sucessfully Added","area_data":area_data})
        except IntegrityError :
            return render(request,"empdatabase/master/area.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Area Master","message":"This Area name is already there in our Database","area_data":area_data})
        except Exception as err:
            print(err)
    return render(request,"empdatabase/master/area.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Area Master","obj13":"Style = display:none;","area_data":area_data})

def gstmaster(request):
    gstdata = GSTMaster.objects.all().order_by('S_no')
    if request.POST:
        try :
            gst_head = request.POST.get("head")
            gst_get = request.POST.get("hsn_sac")
            gst_app = request.POST.get("lock")
            if gst_app == "Yes":
                gst = GSTMaster.objects.create(Head=gst_head,HSN_SAC=gst_get,gst=True)
            else :
                gst = GSTMaster.objects.create(Head=gst_head,HSN_SAC=gst_get,gst=False)
            gst.save()
            gst_ = GSTMaster.objects.get(Head=gst_head)
            gst_.S_no = len(gstdata)
            gst_.save()
            gstdata = GSTMaster.objects.all().order_by('S_no')
            return render(request,"empdatabase/master/gstmaster.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"GST Master","message":"GST Head has been sucessfully added","gstdata":gstdata})
        except IntegrityError :
            return render(request,"empdatabase/master/gstmaster.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"GST Master","message":"This GST Head is already there in our database","gstdata":gstdata})
        except Exception as err:
            print(err)
    return render(request,"empdatabase/master/gstmaster.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"GST Master","obj13":"Style = display:none;","gstdata":gstdata})

def sectormaster(request):
    sec_data = SectorName.objects.all().order_by('S_no')
    pro_data = ProjectName.objects.all().order_by('Project_Name')
    if request.POST:
        try :
            sec_d = request.POST.get("sector_name")
            sel = request.POST.get("proj")
            pro = ProjectName.objects.get(Project_Name=sel)
            SectorName.objects.get(ProjectName=pro,Sector_Name=sec_d)
            msg = "for {} this Sector is already in our Database".format(sel)
            return render(request,"empdatabase/master/sector.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Sector Master","message":msg,"sec_data":sec_data,"pro_data":pro_data})
        except SectorName.DoesNotExist:
            sec = SectorName.objects.create(ProjectName=pro,Sector_Name=sec_d)
            sec.save()
            sec_ = SectorName.objects.get(ProjectName=pro,Sector_Name=sec_d)
            sec_.S_no = len(sec_data)
            sec_.save()
            sec_data = SectorName.objects.all().order_by('S_no')
            return render(request,"empdatabase/master/sector.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Sector Master","message":"Sector has been added sucessfully","sec_data":sec_data,"pro_data":pro_data})
    return render(request,"empdatabase/master/sector.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Sector Master","obj13":"Style = display:none;","sec_data":sec_data,"pro_data":pro_data})

def plotaddmaster(request):
    pm = PlotMaster.objects.all()
    plt_type = Plottype.objects.all().order_by('Plottype')
    plt_flag = PlotFlag.objects.all().order_by('Plot_Flag_Name')
    sec_ = SectorName.objects.all().order_by('Sector_Name')
    cat_ = CategoryName.objects.all().order_by('Category_Name')
    area_ = AreaName.objects.all().order_by('Area_Name')
    pro_data = ProjectName.objects.all().order_by('Project_Name')
    if request.POST :
        proj = request.POST.get('proj')
        block = request.POST.get('block')
        block = block.split('-')[1]
        plotno = request.POST.get('plotno')
        plotsize = request.POST.get('plotsize')
        extra = request.POST.get('extra')
        type = request.POST.get('type')
        cat = request.POST.get('cat')
        area = request.POST.get('area')
        ttyp = request.POST.get('ttyp')
        tag = request.POST.get('tag')
        flag = request.POST.get('flag')
        ptype = Plottype.objects.get(Plottype=type)
        pflag = PlotFlag.objects.get(Plot_Flag_Name=flag)
        sec = SectorName.objects.get(Sector_Name=block)
        cat = CategoryName.objects.get(Category_Name=cat)
        area = AreaName.objects.get(Area_Name=area)
        pdata = ProjectName.objects.get(Project_Name=proj)
        plot_a = PlotMaster.objects.create(Project=pdata,Sector=sec,Plot_no=plotno,Plot_size=plotsize,
        Extra_Land=extra,Plot_type=ptype,Plot_Category=cat,Plot_Area=area,Type=ttyp,Tag=tag,Flag=pflag)
        plot_a.save() 
        plot_a = PlotMaster.objects.get(Plot_no=plotno)
        plot_a.S_no = len(pm)
        plot_a.save()
        return render(request,"empdatabase/master/plotadd.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Add Plot Master","message":"Plot has been added sucessfully",
    'plt_type':plt_type,'plt_flag':plt_flag,'sec_':sec_,'cat_':cat_,'area_':area_,'pro_data':pro_data})

    return render(request,"empdatabase/master/plotadd.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Add Plot Master","obj13":"Style = display:none;",
    'plt_type':plt_type,'plt_flag':plt_flag,'sec_':sec_,'cat_':cat_,'area_':area_,'pro_data':pro_data})

def allplot(request):
    return render(request,"empdatabase/master/tabledata.html")


####Master Edit Section#####
def plottypeedit(request):
    Id = request.GET.get("Id")
    plot_data = Plottype.objects.get(id=Id)
    if request.POST :
        name = request.POST.get("type_name")
        if name == None or name == "":
            pass
        else :
           plot_data.Plottype = name 
           plot_data.save()
        return redirect("/employeedb/master/plottypemaster/") 
    return render(request,"empdatabase/master/plottypeedit.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Plot Type Master","obj3":"Style = display:none;","plot":plot_data})

def projedit(request):
    Id = request.GET.get("Id")
    proj_data = ProjectName.objects.get(id=Id)
    if request.POST :
        name = request.POST.get("type_name")
        if name == None or name == "":
            pass
        else :
           proj_data.Project_Name = name
           proj_data.save()
        return redirect("/employeedb/master/projectmaster/") 
    return render(request,"empdatabase/master/projedit.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Plot Type Master","obj3":"Style = display:none;","proj_data":proj_data})

def plotflagedit(request):
    Id = request.GET.get("Id")
    pflag_data = PlotFlag.objects.get(id=Id)
    if request.POST :
        name = request.POST.get("type_name")
        if name == None or name == "":
            pass
        else :
           pflag_data.Plot_Flag_Name = name
           pflag_data.save()
        return redirect("/employeedb/master/plotflagmaster/")
    return render(request,"empdatabase/master/pltflg.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Plot Flag Master","pflag_data":pflag_data,"obj13":"Style = color:#FFF5F9;"})

def areaedit(request):
    Id = request.GET.get("Id")
    area_data = AreaName.objects.get(id=Id)
    if request.POST :
        name = request.POST.get("type_name")
        if name == None or name == "":
            pass
        else :
           area_data.Area_Name = name
           area_data.save()
        return redirect("/employeedb/master/areamaster/")
    return render(request,"empdatabase/master/areaedit.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Area Master","area_data":area_data})
    
def categoryedit(request):
    Id = request.GET.get("Id")
    cat_data = CategoryName.objects.get(id=Id)
    if request.POST :
        name = request.POST.get("type_name")
        if name == None or name == "":
            pass
        else :
           cat_data.Category_Name = name
           cat_data.save()
        return redirect("/employeedb/master/categorymaster/")
    return render(request,"empdatabase/master/categoryedit.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Category Master","obj3":"Style = display:none;","cat_data":cat_data})


def gstedit(request):
    Id = request.GET.get("Id")
    gst_data = GSTMaster.objects.get(id=Id)
    if request.POST :
        head = request.POST.get("head")
        hsn = request.POST.get("hsn_sac")
        gst = request.POST.get("lock")
        if head == None or head == "":
            return render(request,"empdatabase/master/gstmasteredit.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"GST Master","message":"Head cannot be null","gst_data":gst_data})
        else :
           gst_data.Head = head
           gst_data.HSN_SAC = hsn
           if gst == "Yes" :
            gst_data.gst=True
           else :
            gst_data.gst=False
           gst_data.save()
        return redirect("/employeedb/master/gstmaster/")
    return render(request,"empdatabase/master/gstmasteredit.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"GST Master","obj3":"Style = display:none;","gst_data":gst_data})

def sectoredit(request):
    Id = request.GET.get("Id")
    sec_data = SectorName.objects.get(id=Id)
    pro_data = ProjectName.objects.all().order_by('Project_Name')
    if request.POST:
        proj_name = request.POST.get("proj")
        sec_name = request.POST.get("sector_name")
        pro_obj = ProjectName.objects.get(Project_Name=proj_name)
        sec_data.ProjectName = pro_obj
        sec_data.Sector_Name = sec_name
        sec_data.save()
        return redirect("/employeedb/master/sectormaster/")
    return render(request,"empdatabase/master/sectoredit.html",{"obj1":"Style = color:#FFF5F9;",'newclr1':'newclr',"page":"Master","subpage":"Sector Master","obj3":"Style = display:none;","sec_data":sec_data,"pro_data":pro_data})


####Master Delete Section####


def plottypedel(request):
    Id = request.GET.get("Id")
    plot_data = Plottype.objects.get(id=Id)
    sno = plot_data.S_no
    plot_data.delete()
    try : 
        last = Plottype.objects.latest('id')
        if last.S_no < sno :
            pass
        else :
            last.S_no = sno
            last.save()
    except Exception:
        pass
    return redirect("/employeedb/master/plottypemaster/")

def projdel(request):
    Id = request.GET.get("Id")
    proj_data = ProjectName.objects.get(id=Id)
    sno = proj_data.S_no
    proj_data.delete()
    try :
        last = ProjectName.objects.latest('id')
        if last.S_no < sno :
            pass
        else :
            last.S_no = sno
            last.save()
    except Exception:
        pass
    return redirect("/employeedb/master/projectmaster/")

def plotflagdel(request):
    Id = request.GET.get("Id")
    plt_data = PlotFlag.objects.get(id=Id)
    
    sno = plt_data.S_no
    plt_data.delete()
    try :
        last = PlotFlag.objects.latest('id')
        if last.S_no < sno :
            pass
        else :
            last.S_no = sno
            last.save()
    except Exception:
        pass
    return redirect("/employeedb/master/plotflagmaster/")



def categorydel(request):
    Id = request.GET.get("Id")
    plt_data = CategoryName.objects.get(id=Id)
    
    sno = plt_data.S_no
    plt_data.delete()
    try :
        last = CategoryName.objects.latest('id')
        if last.S_no < sno :
            pass
        else :
            last.S_no = sno
            last.save()
    except Exception:
        pass
    return redirect("/employeedb/master/categorymaster/")

def areadel(request):
    Id = request.GET.get("Id")
    plt_data = AreaName.objects.get(id=Id)
    
    sno = plt_data.S_no
    plt_data.delete()
    try :
        last = AreaName.objects.latest('id')
        if last.S_no < sno :
            pass
        else :
            last.S_no = sno
            last.save()
    except Exception:
        pass
    return redirect("/employeedb/master/areamaster/")

def gstdel(request):
    Id = request.GET.get("Id")
    gst_data = GSTMaster.objects.get(id=Id)
    
    sno = gst_data.S_no
    gst_data.delete()
    try :
        last = GSTMaster.objects.latest('id')
        if last.S_no < sno :
            pass
        else :
            last.S_no = sno
            last.save()
    except Exception:
        pass
    return redirect("/employeedb/master/gstmaster/")


def sectordel(request):
    Id = request.GET.get("Id")
    sec_data = SectorName.objects.get(id=Id)
    
    sno = sec_data.S_no
    sec_data.delete()
    try :
        last = SectorName.objects.latest('id')
        if last.S_no < sno :
            pass
        else :
            last.S_no = sno
            last.save()
    except Exception:
        pass
    return redirect("/employeedb/master/sectormaster/")



def usermasterdel(request):
    user = request.GET.get("Id")
    userm = MasterUser.objects.get(id=user)
    userpro = User.objects.get(username=userm.user)
    userpro.delete()
    return redirect("/employeedb/master/usermaster/")