# Generated by Django 3.2 on 2022-03-02 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("conferences", "0011_delete_resource"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "polymorphic_ctype",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polymorphic_conferences.resource_set+",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "talk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resources",
                        to="conferences.talk",
                    ),
                ),
            ],
            options={
                "verbose_name": "Resource",
                "verbose_name_plural": "resources",
                "db_table": "resources",
            },
        ),
        migrations.CreateModel(
            name="ResourceFile",
            fields=[
                (
                    "resource_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="conferences.resource",
                    ),
                ),
                ("file", models.FileField(upload_to="resources/")),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("conferences.resource",),
        ),
        migrations.CreateModel(
            name="ResourceImage",
            fields=[
                (
                    "resource_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="conferences.resource",
                    ),
                ),
                ("file", models.ImageField(upload_to="resources/")),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("conferences.resource",),
        ),
        migrations.CreateModel(
            name="ResourceLink",
            fields=[
                (
                    "resource_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="conferences.resource",
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        blank=True, default=None, max_length=200, null=True
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("conferences.resource",),
        ),
    ]