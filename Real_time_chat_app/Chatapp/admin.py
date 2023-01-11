from django.contrib import admin
from .models import*

# Register your models here.
admin.site.site_header = 'Django Chat'
admin.site.site_title = 'Django Chat'
admin.site.index_title = 'Django Chat'

admin.site.register(Room)

@admin.register(Chat)
class ChatModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'timestamp', 'group']

@admin.register(Group)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

