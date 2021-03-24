from django.contrib import admin

# Register your models here.

from .models import Photo, category

admin.site.register(category)
admin.site.register(Photo)