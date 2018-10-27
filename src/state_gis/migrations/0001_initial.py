# Generated by Django 2.1.1 on 2018-10-27 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('block_gis', models.FileField(blank=True, null=True, upload_to='state_gis/blocks')),
                ('block_count', models.IntegerField(blank=True, null=True)),
                ('county_gis', models.FileField(blank=True, null=True, upload_to='state_gis/counties/')),
                ('county_count', models.IntegerField(blank=True, null=True)),
                ('precinct_gis', models.FileField(blank=True, null=True, upload_to='state_gis/precincts/')),
                ('precinct_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]