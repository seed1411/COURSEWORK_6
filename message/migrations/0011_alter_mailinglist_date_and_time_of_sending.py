# Generated by Django 4.2.2 on 2024-08-25 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0010_mailinglist_date_and_time_of_sending"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailinglist",
            name="date_and_time_of_sending",
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                null=True,
                verbose_name="Дата и время первой отправки отправки",
            ),
        ),
    ]