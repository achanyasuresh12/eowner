# Generated by Django 2.0.7 on 2018-11-11 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Managers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mgrname', models.CharField(default='', max_length=20)),
                ('mgrhouse', models.CharField(default='', max_length=20)),
                ('mgrplace', models.CharField(default='', max_length=20)),
                ('mgrcity', models.CharField(default='', max_length=20)),
                ('mgremail', models.CharField(default='', max_length=50)),
                ('mgrgender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=10)),
                ('mgrdob', models.DateField(default=datetime.date.today)),
                ('mgrage', models.IntegerField()),
                ('mgrcontact', models.CharField(default='', max_length=15)),
                ('mgrusername', models.CharField(default='', max_length=20)),
                ('mgrpassword', models.CharField(default='', max_length=20)),
                ('mgrdate_of_join', models.DateField(default=datetime.date.today)),
                ('mgrstatus', models.CharField(default='', max_length=20)),
                ('mgrqualification', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
