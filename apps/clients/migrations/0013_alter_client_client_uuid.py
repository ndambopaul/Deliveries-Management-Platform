# Generated by Django 5.1.1 on 2024-09-20 07:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0012_alter_client_client_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="client_uuid",
            field=models.UUIDField(
                default=uuid.UUID("30728ae4-40e8-41bc-bb91-6996ba2a2c1f")
            ),
        ),
    ]
