import datetime
import os
from django.db import models

# Create your models here.

def upload_path_category(instance, filename):
    return os.path.join('category/' + datetime.datetime.now().strftime('%Y/%m/%d/') + instance.title, filename)

class recmd(models.Model):
    pattern=models.CharField(max_length=50,default="foobar" )
    predection=models.CharField(max_length=50 ,default="foobar")
    img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.predection 

class recmd1(models.Model):
    pattern=models.CharField(max_length=50,default="pattern" )
    predection=models.CharField(max_length=50 ,default="pattern")
    img = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.predection 

class Category(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=120)
    img = models.ImageField(upload_to = upload_path_category, height_field=None, width_field=None, blank=True, default=True, null=True)
    desc = models.TextField(null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  