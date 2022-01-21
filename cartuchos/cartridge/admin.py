from django.contrib import admin
from django.urls import path
from django import forms
import csv
import io
from django.shortcuts import redirect, render

# Register your models here.
from .models import Cartridges, Manufacturer, Family, SubFamilyIntern, SubFamily, \
                    Reference, ColorReference, Color, Size, Clase, GroupUnity, \
                    ReferenceGroup, FboCode


@admin.register(GroupUnity)
class GroupUnityAdmin(admin.ModelAdmin):
    pass


@admin.register(ReferenceGroup)
class ReferenceGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(FboCode)
class FboCodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass


@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    pass


@admin.register(ColorReference)
class ColorReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(SubFamily)
class SubFamilyAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    pass


@admin.register(SubFamilyIntern)
class SubFamilyInternAdmin(admin.ModelAdmin):
    pass


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Cartridges)
class CartridgesAdmin(admin.ModelAdmin):
    change_list_template = "cartridge/cartridge_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = io.TextIOWrapper(request.FILES["csv_file"].file, encoding='utf-8')
            reader = csv.reader(csv_file)
            
            counter = 0
            for row in reader:
                if counter == 0:  #  They are the HEADERS
                    counter += 1
                    continue
                
                code = row[1]
                _manufacturer = row[2]
                _family = row[3]
                _sub_family_intern = row[4]
                _family_intern = row[5]
                _reference = row[6]
                _color_reference = row[9]
                _color = row[10]
                _size = row[11]
                _clase = row[12]
                date = row[13]
                _group_unity = row[14]
                _reference_group = row[15]
                _fbo_code = row[16]
                
                try:
                    selling_price_base = float(row[7])
                except:
                    selling_price_base = 0
                
                try:
                    weitgh = int(row[8])
                except:
                    weitgh = 0
                
                manufacturer, _ = Manufacturer.objects.get_or_create(name=_manufacturer)
                family, _ = Family.objects.get_or_create(name=_family)
                sub_family_intern, _ = SubFamilyIntern.objects.get_or_create(name=_sub_family_intern)
                family_intern, _ = SubFamily.objects.get_or_create(name=_family_intern)
                reference, _ = Reference.objects.get_or_create(name=_reference)
                color_reference, _ = ColorReference.objects.get_or_create(name=_color_reference)
                color, _ = Color.objects.get_or_create(name=_color)
                size, _ = Size.objects.get_or_create(value=_size)
                clase, _ = Clase.objects.get_or_create(name=_clase)
                group_unity, _ = GroupUnity.objects.get_or_create(name=_group_unity)
                reference_group, _ = ReferenceGroup.objects.get_or_create(name=_reference_group)
                fbo_code, _ = FboCode.objects.get_or_create(name=_fbo_code)
                
                cartridges, _ = Cartridges.objects.get_or_create(
                    code=code,
                    selling_price_base=selling_price_base,
                    weitgh=weitgh,
                    date=date,
                    manufacturer=manufacturer,
                    family=family,
                    sub_family_intern=sub_family_intern,
                    family_intern=family_intern,
                    reference=reference,
                    color_reference=color_reference,
                    color=color,
                    size=size,
                    clase=clase,
                    group_unity=group_unity,
                    reference_group=reference_group,
                    fbo_code=fbo_code)
                
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "custom/csv_form.html", payload
        )