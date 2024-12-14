from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user_image = models.ImageField(upload_to="images")
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=150, unique=True)
