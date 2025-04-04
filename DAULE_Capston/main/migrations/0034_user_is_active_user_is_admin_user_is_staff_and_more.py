# Generated by Django 4.1.7 on 2023-06-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0033_remove_user_is_active_remove_user_is_admin_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default="", max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.TextField(default="", max_length=10),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(default="", max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name="student", name="studentID", field=models.IntegerField(),
        ),
    ]
