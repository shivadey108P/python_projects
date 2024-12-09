from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    username = models.CharField(max_length=100, null=False)
    review_text = models.TextField(null=False)
    rating = models.IntegerField(null=False, validators=[
        MinValueValidator(1), MaxValueValidator(5),
    ])
