from django.contrib import admin

# Register your models here.
from .models import ReportDefinition, ReportRequest


@admin.register(ReportDefinition)
class ReportDefinitionAdmin(admin.ModelAdmin):
    pass


@admin.register(ReportRequest)
class ReportRequestAdmin(admin.ModelAdmin):
    pass

