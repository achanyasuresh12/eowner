# Generated by Django 2.0.7 on 2018-09-07 17:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('busdetails', '0002_busdetails_seatorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticketbooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('source', models.CharField(default='', max_length=20)),
                ('destination', models.CharField(default='', max_length=20)),
                ('seat', models.IntegerField()),
                ('duration', models.CharField(default='', max_length=20)),
                ('dropping_points', models.CharField(default='', max_length=20)),
                ('fare', models.CharField(default='', max_length=20)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busdetails.Busdetails')),
            ],
        ),
    ]
