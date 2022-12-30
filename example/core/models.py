from django.db import models

# Create your models here.
 
class Contact(models.Model): 
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    message=models.CharField(max_length=122)