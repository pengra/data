# Generated by Django 2.1.2 on 2018-10-10 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordindex', '0003_auto_20181005_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wordindex',
            options={'ordering': ('-count',)},
        ),
    ]