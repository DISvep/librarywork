from django.contrib import admin
from .models import LibraryBook


# Register your models here.
class LibraryBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available')
