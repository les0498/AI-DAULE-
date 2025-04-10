# Generated by Django 4.1.7 on 2023-05-29 17:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_response"),
    ]

    operations = [
        migrations.RemoveField(model_name="question", name="question_text",),
        migrations.AddField(
            model_name="question",
            name="text",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
        ),
        migrations.AlterField(
            model_name="response",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.question"
            ),
        ),
    ]
