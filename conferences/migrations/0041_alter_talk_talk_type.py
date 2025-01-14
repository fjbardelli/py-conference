# Generated by Django 3.2 on 2022-08-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0040_auto_20220717_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='talk_type',
            field=models.CharField(blank=True, choices=[('talk', 'Talk'), ('workshop', 'Workshop/Taller'), ('keynote', 'Keynote/Charla magistral'), ('lightning_talk', 'Lightning Talk'), ('sprints', 'Sprints'), ('open_space', 'Open Space'), ('panel', 'Panel')], default=None, max_length=30, null=True),
        ),
    ]
