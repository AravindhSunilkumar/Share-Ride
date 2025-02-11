# app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username



class add_profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profileimg = models.ImageField(upload_to='profiles', null=True, blank=True)
    vehicle_name = models.CharField(max_length=25, null=True, blank=True)
    vehicle_number = models.CharField(max_length=15, null=True, blank=True)
    vehicle_img = models.ImageField(upload_to='profiles', null=True, blank=True)
    new_field = models.CharField(max_length=50, null=True, blank=True)  # New field

    # def __str__(self):
    #     return self.name


class vehicle_owner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Add a default value, you can change it as needed
    name = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profileimg = models.ImageField(upload_to='profiles', null=True, blank=True)
    vehicle_name = models.CharField(max_length=25, null=True, blank=True)
    vehicle_number = models.CharField(max_length=15, null=True, blank=True)
    vehicle_img = models.ImageField(upload_to='profiles', null=True, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=25, null=True, blank=True)
    def __str__(self):
        return f"{self.user_name} booked {self.driver_name}"


