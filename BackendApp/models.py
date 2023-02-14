from django.db import models

# Create your models here.
class admindb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    MobileNumber = models.IntegerField(null=True,blank=True)
    EmailID = models.EmailField(null=True,blank=True)
    UserName = models.CharField(max_length=50,null=True,blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)
    ConfirmPassword = models.CharField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to="profile")

class categorydb(models.Model):
    VehicleType = models.CharField(max_length=50, blank=True, null=True)
    VehicleNumber=models.IntegerField(null=True,blank=True)
    VehicleModel=models.CharField(max_length=50, blank=True, null=True)
    VehicleDescription =models.CharField(max_length=50, blank=True, null=True)
    Image =models.ImageField(upload_to="profile")

class Vehicledatabase(models.Model):
    VehicleType = models.CharField(max_length=50, null=True, blank=True)
    ProductName = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Color = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="profile")


class Contactdb(models.Model):
    Name=models.CharField(max_length=50, null=True, blank=True)
    EmailID=models.EmailField(max_length=50, null=True, blank=True)
    Subject = models.CharField(max_length=50, null=True, blank=True)
    Message=models.CharField(max_length=100, null=True, blank=True)

class Bookingdb(models.Model):
    Name=models.CharField(max_length=50, null=True, blank=True)
    EmailID=models.EmailField(max_length=50, null=True, blank=True)
    Number=models.IntegerField(null=True,blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    VehicleDetails=models.CharField(max_length=100, null=True, blank=True)