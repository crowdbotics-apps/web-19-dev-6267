# Generated by Django 2.2.13 on 2020-06-19 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_homepage_sdcasc"),
    ]

    operations = [
        migrations.RemoveField(model_name="homepage", name="sdcasc",),
    ]
