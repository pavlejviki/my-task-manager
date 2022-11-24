# Generated by Django 3.2.16 on 2022-11-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_alter_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.IntegerField(
                choices=[(2, "High"), (4, "Low"), (3, "Medium"), (1, "Urgent")]
            ),
        ),
    ]
