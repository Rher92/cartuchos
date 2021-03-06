# Generated by Django 3.2.11 on 2022-02-12 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0004_auto_20220211_2230'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cartridge', '0002_auto_20220211_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteCodeReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', null=True, verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('number', models.IntegerField(default=1)),
                ('prefix', models.CharField(blank=True, default='A', max_length=10, null=True)),
            ],
            options={
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SelectedCartridges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', null=True, verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('Cartridges', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cartridges', related_query_name='cartridges', to='cartridge.cartridges')),
            ],
            options={
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', null=True, verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('box_weight', models.FloatField()),
                ('total_weight', models.FloatField()),
                ('laser_weight', models.FloatField()),
                ('laser_percent', models.FloatField()),
                ('inkjet_weight', models.FloatField()),
                ('inkjet_percent', models.FloatField()),
                ('total_items', models.IntegerField()),
                ('code', models.CharField(blank=True, max_length=30, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('cartridges', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cartridges', related_query_name='cartridges', to='note.selectedcartridges')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='client', related_query_name='client', to='clients.cliente')),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salesman', related_query_name='salesman', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Albaran',
                'verbose_name_plural': 'Albaranes',
            },
        ),
    ]
