# Generated by Django 4.2 on 2023-04-17 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="emp",
            old_name="comm",
            new_name="comission",
        ),
    ]
