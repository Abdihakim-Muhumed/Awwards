from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=30)
    landing_page = CloudinaryField('image')
    description = models.CharField(max_length=150)
    link = models.CharField(max_length=100)

    def save_profile(self):
         self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.username