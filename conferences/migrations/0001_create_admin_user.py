# Generated by Django 3.2 on 2022-02-28 16:07

from django.db import migrations
from django.contrib.auth.models import User


def create_admin_user(apps, schema_editor):
    User.objects.create_superuser(
        username="admin", password="asdasd123", email="admin@admin.com"
    )


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunPython(create_admin_user, migrations.RunPython.noop),
    ]