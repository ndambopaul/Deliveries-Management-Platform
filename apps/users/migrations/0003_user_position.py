# Generated by Django 5.1.1 on 2024-09-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_tenant"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="position",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
