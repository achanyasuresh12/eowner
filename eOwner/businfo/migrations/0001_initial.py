# Generated by Django 2.0.7 on 2018-10-26 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('busdetails', '0009_remove_busdetails_dropping_point'),
    ]

    operations = [
        migrations.CreateModel(
            name='Businfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropping_points', models.CharField(default='', max_length=20)),
                ('mgr_id', models.BigIntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busdetails.Busdetails')),
            ],
        ),
    ]
