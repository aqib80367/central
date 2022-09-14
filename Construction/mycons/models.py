from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=122)
    number = models.CharField(max_length=122)
    # address = models.CharField(max_length=122)
    # address2 = models.CharField(max_length=122)
      
    zip = models.CharField(max_length=10)


    
