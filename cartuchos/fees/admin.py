from django.contrib import admin
from django.urls import path
from django import forms
import csv
import io
from django.shortcuts import redirect, render

# Register your models here.

from .models import Fees
from cartuchos.cartridge.models import Family, SubFamilyIntern


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    change_list_template = "fees/fees_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = io.TextIOWrapper(request.FILES["csv_file"].file, encoding='utf-8')
            # reader = csv.reader(csv_file)
            reader = csv.reader(x.replace('\0', '') for x in csv_file)

            
            counter = 0
            for row in reader:
                if counter == 0:  #  They are the HEADERS
                    fees_name = row[2:]
                    counter += 1
                    continue
                
                _family = row[0]
                _sub_family_intern = row[1]
                              
                family, _ = Family.objects.get_or_create(name=_family)
                sub_family_intern, _ = SubFamilyIntern.objects.get_or_create(name=_sub_family_intern)
                fees = row[2:]
                
                dict_fees_name = tuple(zip(fees_name, fees))
                
                for item in dict_fees_name:
                    _name = item[0]
                    try:
                        _fee = float(item[1])
                    except:
                        _fee = float(0)

                    feex, _ = Fees.objects.get_or_create(
                        name=_name,
                        fee=_fee,
                        family=family,
                        sub_family_intern=sub_family_intern
                    )
                
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "custom/csv_form.html", payload
        )