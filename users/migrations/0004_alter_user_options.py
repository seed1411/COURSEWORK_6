# Generated by Django 4.2.2 on 2024-09-01 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ("id",),
                "permissions": [("can_edit_is_active", "can_edit_is_active")],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
