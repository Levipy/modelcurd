from django.contrib import admin
from .models import BlogModel,TagModel
# Register your models here.

admin.site.register(BlogModel)
admin.site.register(TagModel)