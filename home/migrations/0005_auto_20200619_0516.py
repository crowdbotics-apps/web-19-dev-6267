# Generated by Django 2.2.13 on 2020-06-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_remove_customtext_sfdwaf"),
    ]

    operations = [
        migrations.RemoveField(model_name="customtext", name="sdfwafe",),
        migrations.AddField(
            model_name="customtext",
            name="sfdwaf",
            field=models.TextField(blank=True, null=True),
        ),
    ]
