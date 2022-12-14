# Generated by Django 3.2.16 on 2022-12-01 10:57

import apps.home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_rename_image_worker_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worker",
            name="profile_image",
            field=models.ImageField(
                blank=True, null=True, upload_to=apps.home.models.worker_image_file_path
            ),
        ),
    ]
