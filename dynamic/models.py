from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=20,default="")
    mail = models.EmailField(max_length=30,default="")
    message = models.TextField(max_length=1000,default="")
    
    class Metta:
        dp_table = "contact"
        
class job(models.Model):
    firstname = models.CharField(max_length=50,default="")
    secondname = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=10)
    experience = models.CharField(max_length=50)
    mail = models.EmailField(max_length=30,default="")
    Resume = models.FileField()       
        
    class Metta:
        dp_table = "job_apply"     
        
class details(models.Model):
    name = models.CharField(max_length=50,default="")
    mail = models.EmailField(max_length=30,default="")
    tellAboutUs=models.CharField(max_length=1000)
    message = models.CharField(max_length=10000)       
        
    class Metta:
        dp_table = "details"         
        
         