# Generated by Django 5.0.4 on 2024-05-04 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_datetime', models.DateTimeField()),
                ('service_type', models.CharField(choices=[('VAC', 'Vaccination'), ('CHK', 'Checkup'), ('SUR', 'Surgery'), ('OTH', 'Other')], max_length=3)),
                ('status', models.CharField(choices=[('PEN', 'Pending'), ('CON', 'Confirmed'), ('CAN', 'Cancelled')], default='PEN', max_length=3)),
                ('reason_for_visit', models.TextField(blank=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
                ('pet_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]