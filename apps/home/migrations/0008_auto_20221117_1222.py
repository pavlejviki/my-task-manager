# Generated by Django 3.2.16 on 2022-11-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_auto_20221117_1202"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["is_completed", "-priority"]},
        ),
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[("Low", "4"), ("High", "2"), ("Medium", "3"), ("Urgent", "1")],
                max_length=6,
            ),
        ),
    ]
