# Generated by Django 4.2.2 on 2023-06-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clinic_app", "0003_alter_appointment_appointment_datetime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clinic",
            name="feature_image",
            field=models.ImageField(default="images/default.png", upload_to="images/"),
        ),
    ]
