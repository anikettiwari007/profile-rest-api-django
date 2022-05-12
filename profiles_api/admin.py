from django.contrib import admin
from profiles_api import models

# Register your models here to access it through admin interface.
admin.site.register(models.UserProfile)
