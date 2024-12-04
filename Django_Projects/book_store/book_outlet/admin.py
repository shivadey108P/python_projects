from django.contrib import admin

from .models import Books, Author, Country, Address

# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['title']}
    list_filter = ('author', 'rating')
    list_display = ('title', 'author')

admin.site.register(Books, BooksAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)