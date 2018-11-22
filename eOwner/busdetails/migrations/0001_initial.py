# Generated by Django 2.0.7 on 2018-07-31 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Busdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('regno', models.CharField(default='', max_length=20)),
                ('permitno', models.CharField(default='', max_length=20)),
                ('seat', models.IntegerField()),
                ('source', models.CharField(default='', max_length=30)),
                ('destination', models.CharField(default='', max_length=30)),
                ('description', models.CharField(default='', max_length=40)),
            ],
        ),
    ]
