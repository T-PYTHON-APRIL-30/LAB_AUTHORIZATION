# Generated by Django 4.2.2 on 2023-06-10 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_appointment_patient_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='department',
            field=models.CharField(choices=[('HC', 'Heart Center'), ('EUC', 'euroscience Center'), ('ObC', 'Obesity Center'), ('EYEC', 'Eye Center'), ('ORC', 'Orthopedic Center'), ('PEC', 'Pediatric Center')], max_length=100),
        ),
    ]
