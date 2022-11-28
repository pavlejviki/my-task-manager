# Generated by Django 3.2.16 on 2022-11-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_alter_task_priority"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="position",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["is_completed", "priority", "deadline"]},
        ),
        migrations.AlterModelOptions(
            name="tasktype",
            options={"ordering": ["name"]},
        ),
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.IntegerField(
                choices=[(1, "Urgent"), (2, "High"), (3, "Medium"), (4, "Low")]
            ),
        ),
    ]