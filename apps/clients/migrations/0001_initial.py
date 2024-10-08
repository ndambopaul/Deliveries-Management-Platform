# Generated by Django 5.1.1 on 2024-09-13 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tenants", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("website", models.CharField(max_length=255, null=True)),
                ("address", models.CharField(max_length=255)),
                ("town", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                (
                    "tenant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tenants.tenant"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("order_number", models.CharField(max_length=255)),
                ("customer_name", models.CharField(max_length=255)),
                ("customer_phone", models.CharField(max_length=255)),
                ("customer_location", models.JSONField(max_length=255)),
                ("customer_address", models.CharField(max_length=500)),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("Pending Dispatch", "Pending Dispatch"),
                            ("Dispatched", "Dispatched"),
                            ("Delivered", "Delivered"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="clients.client"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrderStatusUpdate",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "previous_status",
                    models.CharField(
                        choices=[
                            ("Pending Dispatch", "Pending Dispatch"),
                            ("Dispatched", "Dispatched"),
                            ("Delivered", "Delivered"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "next_status",
                    models.CharField(
                        choices=[
                            ("Pending Dispatch", "Pending Dispatch"),
                            ("Dispatched", "Dispatched"),
                            ("Delivered", "Delivered"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "delivery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="clients.order"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
