# Generated by Django 5.0.7 on 2024-08-06 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clients",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите Ф.И.О. получателя",
                        max_length=250,
                        verbose_name="Ф.И.О",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True, max_length=100, null=True, verbose_name="Сообщение"
                    ),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.CreateModel(
            name="Message",
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
                (
                    "title_letter",
                    models.CharField(max_length=100, verbose_name="Тема письма"),
                ),
                (
                    "body_letter",
                    models.TextField(
                        blank=True, null=True, verbose_name="Содержание письма"
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
        migrations.CreateModel(
            name="MailingList",
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
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("DAILY", "Раз в день"),
                            ("WEEKLY", "Раз в неделю"),
                            ("MONTHLY", "Раз в месяц"),
                        ],
                        default="DAILY",
                        max_length=50,
                        verbose_name="Периодичность рассылки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("COMPLETED", "Завершена"),
                            ("CREATED", "Создана"),
                            ("RUNNING", "Запущена"),
                        ],
                        default="CREATED",
                        max_length=50,
                    ),
                ),
                (
                    "clients",
                    models.ManyToManyField(
                        to="message.clients", verbose_name="Клиенты"
                    ),
                ),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="message.message",
                        verbose_name="Сообщение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.CreateModel(
            name="Attempt",
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
                (
                    "date_time_last_attempt",
                    models.DateTimeField(
                        verbose_name="Дата и время последнего попытки отправки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("SUCCESS", "Успешно"), ("FAILURE", "Не успешно")],
                        default="FAILURE",
                        max_length=50,
                        verbose_name="Статус попытки",
                    ),
                ),
                (
                    "mail_server_response",
                    models.TextField(verbose_name="Ответ почтового сервера"),
                ),
                (
                    "mailing_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attempts",
                        to="message.mailinglist",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка",
                "verbose_name_plural": "Попытки",
            },
        ),
    ]