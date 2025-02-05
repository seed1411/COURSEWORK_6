# Generated by Django 4.2.2 on 2024-09-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("tittle", models.CharField(max_length=50, verbose_name="Заголовок")),
                ("content_article", models.TextField(verbose_name="Описание")),
                (
                    "images",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "count_view",
                    models.PositiveIntegerField(
                        default=0, editable=False, verbose_name="Количество просмотров"
                    ),
                ),
                (
                    "published_date",
                    models.DateField(auto_now_add=True, verbose_name="Дата публикации"),
                ),
            ],
            options={
                "verbose_name": "Блог",
                "verbose_name_plural": "Блоги",
            },
        ),
    ]
