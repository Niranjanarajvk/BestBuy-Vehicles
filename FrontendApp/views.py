from django.shortcuts import render,redirect
from BackendApp.models import categorydb,Contactdb,Vehicledatabase,Bookingdb
from FrontendApp.models import CustomerDetails
from django.contrib import messages

# Create your views here.


# Create your views here.
def index(request):
    data = categorydb.objects.all()
    return render(request,'Index.html',{'data':data})

def aboutpage(request):
    data = categorydb.objects.all()
    return render(request,'About.html',{'data':data})
def blogpg(request):
    data = categorydb.objects.all()
    return render(request,'Blog.html',{'data':data})
def contactpg(request):
    data = categorydb.objects.all()
    return render(request,'Contact.html',{'data':data})

def Contactdatabase(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        sb=request.POST.get('sub')
        ms=request.POST.get('msg')
        obj=Contactdb(Name=na,EmailID=em,Subject=sb,Message=ms)
        obj.save()
    return redirect(contactpg)

def categorydisplaypg(request,itemCatg):
    data = categorydb.objects.all()
    print("===itemCatg===", itemCatg)
    catg = itemCatg.upper()
    products=Vehicledatabase.objects.filter(VehicleType=itemCatg)
    context = {
        'products':products,
        'catg':catg,
        'data':data
    }
    return render(request, 'Categorydisplay.html',context)

def loginadmin(request):
    data=categorydb.objects.all()
    return render(request,'LoginReg.html',{'data':data})
def signuppg(request):
    data = categorydb.objects.all()
    return render(request,'Registration.html',{'data':data})
def customersave(request):
    if request.method=="POST":
        un=request.POST.get('username')
        em=request.POST.get('email')
        pw=request.POST.get('password')
        cp=request.POST.get('confirmpassword')
        if pw==cp:
            obj = CustomerDetails(username=un,email=em,password=pw,confirmpassword=cp)
            obj.save()
            return redirect(loginadmin)
        else:
         return render(request, 'Registration.html')

def customerlogin(request):
    if request.method=='POST':
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if CustomerDetails.objects.filter(username=username_r,password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r

            return redirect(index)
        else:
            messages.warning(request,"sorry.... invalid username or password")
    return render(request, 'LoginReg.html')

def customerlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(index)

def Productdetails(request):
    data1 =Vehicledatabase.objects.all()
    data=categorydb.objects.all()
    return render(request, 'Productdisplay.html', {'data1': data1,'data':data})

def displayproduct(request,dataid):
    data = categorydb.objects.all()
    da=Vehicledatabase.objects.get(id=dataid)
    context2 = {
        'data':data,
        'da':da
    }
    return render(request, 'Productdetail.html', context2)

def bookingdatabase(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        nu = request.POST.get('num')
        ad=request.POST.get('add')
        de=request.POST.get('det')
        obj=Bookingdb(Name=na,EmailID=em,Number=nu,Address=ad,VehicleDetails=de)
        obj.save()
    return redirect(index)



