# Generated by Django 5.1.1 on 2024-09-20 10:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0015_alter_client_client_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="client_uuid",
            field=models.UUIDField(
                default=uuid.UUID("8dd0de7e-2261-4750-ade8-2e684886918e")
            ),
        ),
    ]
