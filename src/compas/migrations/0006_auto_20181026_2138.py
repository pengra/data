# Generated by Django 2.1.1 on 2018-10-27 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compas', '0005_merge_20181026_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='assessment_id',
            field=models.IntegerField(),
        ),
    ]