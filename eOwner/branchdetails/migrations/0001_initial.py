# Generated by Django 2.0.7 on 2018-08-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branchdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('city', models.CharField(default='', max_length=20)),
                ('district', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=20)),
                ('contact', models.IntegerField()),
                ('type', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
