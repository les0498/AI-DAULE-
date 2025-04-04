# Generated by Django 4.1.7 on 2023-06-06 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main", "0023_delete_user_delete_userinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("name", models.CharField(max_length=255, unique=True)),
                ("phone_number", models.CharField(max_length=20, unique=True)),
                ("last_login", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="UserInfo",
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
                ("gender", models.TextField(default="None", max_length=100)),
                ("age", models.IntegerField(default=0)),
                ("accent", models.CharField(default="None", max_length=100)),
                ("answer", models.TextField(default="None", max_length=20)),
                ("mbti", models.CharField(default="N/A", max_length=10)),
                ("hobby", models.TextField(default="None", max_length=20)),
                ("music", models.TextField(default="None", max_length=20)),
            ],
        ),
    ]
