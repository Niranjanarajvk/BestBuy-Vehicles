from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    username=models.CharField(max_length=50, null=True, blank=True)
    email=models.EmailField(max_length=50, null=True, blank=True)
    password=models.CharField(max_length=50, null=True, blank=True)
    confirmpassword=models.CharField(max_length=50, null=True, blank=True)