# Generated by Django 4.2.2 on 2024-08-28 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0013_client_owner_mailinglist_owner_message_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailinglist",
            options={
                "permissions": [("can_edit_status", "can_edit_status")],
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
    ]
