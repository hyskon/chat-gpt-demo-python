from django.contrib import admin
from .models import *
# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ('key')

admin.site.register(Conversation)
admin.site.register(Message)