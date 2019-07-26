from django.db import models
from django.contrib.auth.admin import User

# Create your models here.

class UserProfileInfo(models.Model):

    # Don't Inherit from User
    user = models.OneToOneField(User,on_delete='delete')

    # Addtional Attribute

    picture = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.username

