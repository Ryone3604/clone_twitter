from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    doslikes = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='images/', default='defo')
    
    
    def __str__(self):
        return self.content[:30]

class ProSetting(models.Model):
    
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    headphoto = models.ImageField(upload_to='images/', default='defo')
    prophoto = models.ImageField(upload_to='images/', default='defo')
    
    def __str__(self):
        return self.content[:30]
# Create your models here.
