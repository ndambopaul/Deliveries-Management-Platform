# Generated by Django 5.1.1 on 2024-09-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deliveries", "0002_alter_delivery_delivery_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="delivery_status",
            field=models.CharField(
                choices=[
                    ("Created", "Created"),
                    ("Dispatched", "Dispatched"),
                    ("In Transit", "In Transit"),
                    ("Complete", "Complete"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="deliverystatusupdate",
            name="next_status",
            field=models.CharField(
                choices=[
                    ("Created", "Created"),
                    ("Dispatched", "Dispatched"),
                    ("In Transit", "In Transit"),
                    ("Complete", "Complete"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="deliverystatusupdate",
            name="previous_status",
            field=models.CharField(
                choices=[
                    ("Created", "Created"),
                    ("Dispatched", "Dispatched"),
                    ("In Transit", "In Transit"),
                    ("Complete", "Complete"),
                ],
                max_length=255,
            ),
        ),
    ]
