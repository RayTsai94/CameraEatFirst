from django.contrib import admin
from .models import CheckIn

@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'location')
    list_filter = ('date', 'user')
    search_fields = ('user__username', 'location', 'notes')
    date_hierarchy = 'date'
