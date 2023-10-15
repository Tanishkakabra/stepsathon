from django.contrib import admin
from authnc.models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    fields = ['username', 'email']

admin.site.register(CustomUser)