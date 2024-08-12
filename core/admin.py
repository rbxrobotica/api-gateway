from django.contrib import admin
from .models import CustomUser

class CustomModelAdmin(admin.ModelAdmin):
  list_display = ["name", "email"]
  readonly_fields = ["email"]

admin.site.register(CustomUser, CustomModelAdmin)
