# Generated by Django 2.1.1 on 2018-09-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compas', '0003_auto_20180929_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='assessment_id',
            field=models.IntegerField(unique=True),
        ),
    ]
