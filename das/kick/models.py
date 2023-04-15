from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class cost(models.Model):
#     id_user = models.IntegerField(null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     profile_picture = models.FileField( upload_to='profile_picture',null=True)
#     is_cos = models.BooleanField(default=True)
    
#     bio = models.TextField(blank=True)
#     # location = models.CharField(max_length=100, blank=True)
#     sex =models.CharField(max_length=100)

class costummer(models.Model):
    id_user = models.IntegerField()
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    profile_p =models.ImageField( upload_to='profile_p')
    cos =models.BooleanField(default=True,null=True)
    bio = models.TextField(blank=True)
    sex =models.CharField(max_length=100)
