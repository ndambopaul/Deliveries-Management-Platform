# Generated by Django 5.1.1 on 2024-09-20 10:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0016_alter_client_client_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="client_uuid",
            field=models.UUIDField(
                default=uuid.UUID("3cb1fcc7-9620-4e59-b057-d25943585427")
            ),
        ),
    ]
