# Generated by Django 3.2 on 2022-03-01 14:18

from django.db import migrations



def populate_countries(apps, schema):
    Country = apps.get_model('conferences', 'Country')



class Migration(migrations.Migration):
    dependencies = [
        ('conferences', '0008_auto_20220301_0308'),
    ]

    operations = [
        migrations.RunPython(populate_countries, migrations.RunPython.noop),
    ]