from django.contrib import admin
from .models import User, Admin_User

admin.site.register((User, Admin_User))




