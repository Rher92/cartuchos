# Generated by Django 3.2.11 on 2022-02-14 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20220211_2358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notecodereference',
            options={'verbose_name': 'Codigo de Albaran', 'verbose_name_plural': 'Codigo de Albaranes'},
        ),
        migrations.AlterModelOptions(
            name='selectedcartridges',
            options={'verbose_name': 'Cartucho Seleccionado', 'verbose_name_plural': 'Cartuchos Seleccionados'},
        ),
        migrations.AddField(
            model_name='notes',
            name='inkjet_weight_residual',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notes',
            name='laser_weight_residual',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
