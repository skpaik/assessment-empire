# Generated by Django 3.0.4 on 2020-03-11 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="XWing",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "health",
                    models.IntegerField(default=100, help_text="between 0 and 100"),
                ),
                ("cost", models.FloatField(help_text="Cost in US $")),
                ("name", models.CharField(max_length=12000)),
                ("_coordinates", models.CharField(max_length=10000)),
                (
                    "pilot",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DefenceTower",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sector",
                    models.CharField(
                        choices=[("a1", 1), ("a2", 2), ("b1", 3), ("b2", 4)],
                        max_length=1000,
                    ),
                ),
                ("health", models.IntegerField(default=100)),
                ("cost", models.FloatField(help_text="Cost in US $")),
                ("_coordinates", models.CharField(max_length=10000)),
                (
                    "target",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="exhaust_port.XWing",
                    ),
                ),
            ],
        ),
    ]