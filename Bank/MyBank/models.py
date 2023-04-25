from django.db import models

# Create your models here.
class RegisterModel(models.Model):
	Username = models.CharField(max_length=255)
	Password = models.CharField(max_length=255) 

class District(models.Model):
	District=models.CharField(max_length=255)

class BranchModel(models.Model):
	District=models.ForeignKey(District,on_delete=models.CASCADE)
	Branch=models.CharField(max_length=255)

class ApplicationModel(models.Model):
	User=models.ForeignKey(RegisterModel, on_delete=models.CASCADE)
	Name=models.CharField(max_length=255)
	DOB=models.DateField()
	Age=models.CharField(max_length=10)
	Gender=models.CharField(max_length=10)
	Address=models.CharField(max_length=500)
	District=models.ForeignKey(District,on_delete=models.CASCADE)
	Branch=models.ForeignKey(BranchModel,on_delete=models.CASCADE)
	Account=models.CharField(max_length=255)
	Materials=models.CharField(max_length=255)
	Email=models.EmailField(max_length = 255,null=True)
	Phone=models.CharField(max_length=20,null=True)
