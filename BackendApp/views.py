from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from BackendApp.models import admindb, categorydb, Vehicledatabase, Contactdb, Bookingdb
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage


# Create your views here.
def homepage(request):
    return render(request, 'Home.html')


def Adminpage(request):
    return render(request, 'AddAdmin.html')


def Admindatabase(request):
    if request.method == "POST":
        na = request.POST.get('name')
        nu = request.POST.get('number')
        em = request.POST.get('email')
        pw = request.POST.get('pwd')
        cp = request.POST.get('confpwd')
        img = request.FILES['image']
        obj = admindb(Name=na, MobileNumber=nu, EmailID=em, Password=pw, ConfirmPassword=cp, Image=img)
        obj.save()
        return redirect(Adminpage)


def displayadmin(request):
    data = admindb.objects.all()
    return render(request, 'Displayadmin.html', {'data': data})


def editadmin(request, dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(request, 'EditAdmin.html', {'data': data})


def updateadmin(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        nu = request.POST.get('number')
        em = request.POST.get('email')
        pw = request.POST.get('pwd')
        cp = request.POST.get('confpwd')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image
            admindb.objects.filter(id=dataid).update(Name=na, MobileNumber=nu, EmailID=em, Password=pw,
                                                     ConfirmPassword=cp, Image=file)
    return redirect(displayadmin)


def deleteadmin(request, dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)


def Logindetails(request):
    return render(request, 'Login.html')


def adminlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('user')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['user'] = username_r
                request.session['password'] = password_r
                return redirect(homepage)
            else:
                return redirect(Logindetails)
        else:
            return redirect(Logindetails)


def customerlogout(request):
    del request.session['user']
    del request.session['password']
    return redirect(Logindetails)


def categorypage(request):
    return render(request, 'VehicleCategory.html')


def categorypagedb(request):
    if request.method == "POST":
        nu = request.POST.get('number')
        tp = request.POST.get('type')
        md = request.POST.get('model')
        de = request.POST.get('desc')
        img = request.FILES['image']
        obj = categorydb(VehicleNumber=nu, VehicleType=tp, VehicleModel=md, VehicleDescription=de, Image=img)
        obj.save()
    return redirect(categorypage)


def displaycategory(request):
    data = categorydb.objects.all()
    return render(request, 'Displaycategory.html', {'data': data})


def editcategorypage(request, dataid):
    data = categorydb.objects.get(id=dataid)
    print(data)
    return render(request, 'Editcategory.html', {'data': data})


def updatecategorypage(request, dataid):
    if request.method == "POST":
        nu = request.POST.get('number')
        tp = request.POST.get('type')
        md = request.POST.get('model')
        de = request.POST.get('desc')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(VehicleNumber=nu, VehicleType=tp, VehicleModel=md,
                                                    VehicleDescription=de, Image=file)
        return redirect(displaycategory)


def deletecategory(request, dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)


def vehicleadd(request):
    data = categorydb.objects.all()
    return render(request, 'AddProduct.html', {'data': data})


def vehiclepagedb(request):
    if request.method == 'POST':
        ty = request.POST.get('type')
        na = request.POST.get('name')
        pr = request.POST.get('price')
        cl = request.POST.get('color')
        ds = request.POST.get('desc')
        img = request.FILES['image']
        obj = Vehicledatabase(VehicleType=ty, ProductName=na, Price=pr, Color=cl, Description=ds, Image=img)
        obj.save()
    return redirect(vehicleadd)


def displayproduct(request):
    data = Vehicledatabase.objects.all()
    return render(request, 'Displayproduct.html', {'data': data})


def editproduct(request, dataid):
    data = Vehicledatabase.objects.get(id=dataid)
    da = categorydb.objects.all()
    print(data)
    return render(request, 'Editproduct.html', {'data': data, 'da': da})


def updateproduct(request, dataid):
    if request.method == "POST":
        ty = request.POST.get('type')
        na = request.POST.get('name')
        pr = request.POST.get('price')
        cl = request.POST.get('color')
        ds = request.POST.get('desc')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Vehicledatabase.objects.get(id=dataid).Image
            Vehicledatabase.objects.filter(id=dataid).update(VehicleType=ty, ProductName=na, Price=pr, Color=cl,
                                                             Description=ds, Image=file)
    return redirect(displayproduct)


def deleteproduct(request, dataid):
    data = Vehicledatabase.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)


def displaycontactdb(request):
    data = Contactdb.objects.all()
    return render(request, 'Displaycontactdb.html', {'data': data})


def delcontact(request, dataid):
    data = Contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontactdb)


def displaybooking(request):
    data = Bookingdb.objects.all()
    return render(request, 'Booknowdisplay.html', {'data': data})


def delbooking(request, dataid):
    data = Bookingdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaybooking)
