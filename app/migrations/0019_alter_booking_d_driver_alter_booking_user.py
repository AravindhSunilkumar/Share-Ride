# Generated by Django 5.0 on 2024-01-15 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='d_driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings_as_driver', to='app.vehicle_owner'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings_as_user', to='app.vehicle_owner'),
        ),
    ]