# Generated by Django 2.1.1 on 2018-09-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.GenericIPAddressField(unique=True)),
                ('continent', models.CharField(choices=[('AF', 'Africa'), ('AS', 'Asia'), ('EU', 'Europe'), ('NA', 'North America'), ('OC', 'Oceania'), ('SA', 'South America'), ('AN', 'Antartica')], max_length=2)),
                ('country', models.CharField(blank=True, max_length=2, null=True)),
                ('region_code', models.CharField(blank=True, max_length=5, null=True)),
                ('region_name', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('zip', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('language', models.CharField(blank=True, max_length=2, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
