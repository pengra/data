# Generated by Django 2.1.2 on 2018-10-06 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wordindex', '0002_auto_20181005_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordindex',
            name='url',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wordindex.Webpage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wordindex',
            name='word',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wordindex.Word'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='wordindex',
            unique_together={('word', 'url')},
        ),
    ]
