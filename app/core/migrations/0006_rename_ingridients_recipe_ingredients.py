# Generated by Django 3.2.25 on 2025-02-03 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_ingridient_ingredient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingridients',
            new_name='ingredients',
        ),
    ]
