from django.contrib import admin

# Register your models here.
from .models import SelectedCartridges, NoteCodeReference, Notes


@admin.register(SelectedCartridges)
class SelectedCartridgesAdmin(admin.ModelAdmin):
    pass


@admin.register(NoteCodeReference)
class NoteCodeReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    pass