# Generated by Django 5.1.1 on 2024-09-13 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0006_rename_delivery_orderstatusupdate_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="clientorders",
                to="clients.client",
            ),
        ),
        migrations.AlterField(
            model_name="orderstatusupdate",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orderstatuses",
                to="clients.order",
            ),
        ),
    ]
