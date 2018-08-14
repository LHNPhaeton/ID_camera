from django.db import models
from django.contrib.auth.models import User
#from ckeditor_uploader.fields import RichTextUploadingField

class Gallery(models.Model):
    img_name = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    img = models.ImageField()
    content = models.TextField() #RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

class Text(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)