from django.db import models

# Create your models here.
#This is the schema for the various tables

class Item(models.Model):
    Name = models.CharField(max_length=70, blank=False)
    discp = models.CharField(max_lenth = 10)
    image = models.ImageField(help_text="Upload an image of item you Lost if possible")
    doup = models.DateTimeField(auto_now= True)