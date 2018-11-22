# Generated by Django 2.0.7 on 2018-10-30 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaseinvoice', models.CharField(default='', max_length=20)),
                ('purchasedate', models.DateField(default=datetime.date.today)),
                ('purchasegrandtotal', models.CharField(default='', max_length=20)),
                ('mgr_id', models.BigIntegerField()),
            ],
        ),
    ]