# Generated by Django 4.2.2 on 2024-08-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0007_alter_attempt_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attempt",
            name="date_time_last_attempt",
            field=models.DateTimeField(
                auto_now_add=True,
                verbose_name="Дата и время последнего попытки отправки",
            ),
        ),
    ]
