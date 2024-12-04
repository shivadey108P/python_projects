from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    
    class Meta:
        verbose_name_plural = 'Countries'
    
    def __str__(self) -> str:
        return f"{self.country_name}"
class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=8)
    city = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Address Entries'
    
    def __str__(self) -> str:
        return f"{self.street}, {self.city}-{self.postal_code}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.fullname()

class Books(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='author_books')
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    published_countries = models.ManyToManyField(Country, null=False)
    
    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'Book Entries'

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"