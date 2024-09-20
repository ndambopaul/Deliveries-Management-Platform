# Generated by Django 5.1.1 on 2024-09-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deliveries", "0006_alter_delivery_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="deliveryorder",
            name="delivery_cost",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
