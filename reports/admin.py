from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'scam_type', 'location', 'date_reported', 'is_verified', 'user')
    list_filter = ('scam_type', 'is_verified', 'date_reported', 'user')
    search_fields = ('title', 'description', 'location', 'user__username')
    date_hierarchy = 'date_reported'
    raw_id_fields = ('user',) 