# Generated by Django 3.2 on 2022-05-18 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0019_eventregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='conferences.profile'),
        ),
    ]