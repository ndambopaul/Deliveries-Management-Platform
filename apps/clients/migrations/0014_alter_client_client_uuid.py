# Generated by Django 5.1.1 on 2024-09-20 07:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0013_alter_client_client_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="client_uuid",
            field=models.UUIDField(
                default=uuid.UUID("6e0e9310-c022-4428-9b90-a52f108a6510")
            ),
        ),
    ]
