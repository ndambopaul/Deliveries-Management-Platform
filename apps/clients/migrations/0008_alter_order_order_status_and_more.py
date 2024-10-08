# Generated by Django 5.1.1 on 2024-09-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0007_alter_order_client_alter_orderstatusupdate_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("Created", "Created"),
                    ("Pending Dispatch", "Pending Dispatch"),
                    ("Dispatched", "Dispatched"),
                    ("Delivered", "Delivered"),
                    ("Set For Delivery", "Set For Delivery"),
                ],
                default="Pending Dispatch",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="orderstatusupdate",
            name="next_status",
            field=models.CharField(
                choices=[
                    ("Created", "Created"),
                    ("Pending Dispatch", "Pending Dispatch"),
                    ("Dispatched", "Dispatched"),
                    ("Delivered", "Delivered"),
                    ("Set For Delivery", "Set For Delivery"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="orderstatusupdate",
            name="previous_status",
            field=models.CharField(
                choices=[
                    ("Created", "Created"),
                    ("Pending Dispatch", "Pending Dispatch"),
                    ("Dispatched", "Dispatched"),
                    ("Delivered", "Delivered"),
                    ("Set For Delivery", "Set For Delivery"),
                ],
                max_length=255,
            ),
        ),
    ]
