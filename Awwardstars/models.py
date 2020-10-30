from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=30)
    landing_page = CloudinaryField('image')
    description = models.CharField(max_length=150)
    link = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    total_score = models.IntegerField(default=0)
    average = models.IntegerField(default = 0)
    reviews =models.IntegerField(default=0)
    
    def save_projects(self):
         self.save()

    def delete_projects(self):
        self.delete()

    def __str__(self):
        return self.title

class Profile(models.Model):
    bio = models.CharField(max_length=150)
    profile_photo = CloudinaryField('image')
    contact = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def save_profile(self):
         self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.bio

