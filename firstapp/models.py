from django.db import models

# Create your models here.

class Userprofile(models.Model):
	User=models.OneToOneField(User,on_delete=models.CASCADE)
	gender=models.CharField(max_length=10)
	address=models.CharField(max_length=100)
	mobile_number=models.CharField(max_length=12)	