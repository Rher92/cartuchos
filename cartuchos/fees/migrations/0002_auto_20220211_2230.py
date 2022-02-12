# Generated by Django 3.2.11 on 2022-02-12 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fees',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', null=True, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='fees',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at'),
        ),
    ]