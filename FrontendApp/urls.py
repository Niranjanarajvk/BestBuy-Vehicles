from django.urls import path
from FrontendApp import views
urlpatterns = [
    path('',views.index,name='index'),
    path('aboutpage/',views.aboutpage,name='aboutpage'),
    path('blogpg/',views.blogpg,name='blogpg'),
    path('contactpg/', views.contactpg, name='contactpg'),
    path('Contactdatabase/', views.Contactdatabase, name='Contactdatabase'),
    path('categorydisplaypg/', views.categorydisplaypg, name='categorydisplaypg'),
    path('loginadmin/',views.loginadmin,name='loginadmin'),
    path('signuppg/',views.signuppg,name='signuppg'),
    path('customersave/',views.customersave,name='customersave'),
    path('customerlogin/', views.customerlogin, name='customerlogin'),
    path('customerlogout/', views.customerlogout, name='customerlogout'),
    path('categorydisplaypg/<itemCatg>/', views.categorydisplaypg, name='categorydisplaypg'),
    path('Productdetails/',views.Productdetails,name='Productdetails'),
    path('displayproduct/<int:dataid>/', views.displayproduct, name='displayproduct'),
    path('bookingdatabase',views.bookingdatabase,name='bookingdatabase')

]
