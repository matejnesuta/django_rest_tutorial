from django.contrib import admin
from .models import *
# Register your models here.

myModels = [Article]  # iterable list
admin.site.register(myModels)