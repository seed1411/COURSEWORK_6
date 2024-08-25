# Generated by Django 4.2.2 on 2024-08-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0006_alter_attempt_status_alter_mailinglist_periodicity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attempt",
            name="status",
            field=models.CharField(
                choices=[("Успешно", "Успешно"), ("Не успешно", "Не успешно")],
                default="Не успешно",
                max_length=50,
                verbose_name="Статус попытки",
            ),
        ),
    ]