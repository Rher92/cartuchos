from django.urls import path

from .report_views import edit, run, save

app_name = 'report'
urlpatterns = [
    path('edit/<str:report_type>/', edit, name='report_edit'),
    path('run/', run, name='report_run'),
    path('save/<str:report_type>/', save, name='report_save'),
] 