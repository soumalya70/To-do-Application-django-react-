# Generated by Django 5.0.3 on 2024-03-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todolist",
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
                ("activity_name", models.CharField(max_length=100)),
                ("timing", models.TimeField()),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(0, "Started"), (1, "Finished")], default=0
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
