# Generated by Django 2.0.3 on 2018-03-21 14:25

from django.db import migrations, models
import stad.models


class Migration(migrations.Migration):

    dependencies = [
        ('stad', '0008_auto_20180321_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='competition_logo',
            field=models.ImageField(blank=True, null=True, upload_to=stad.models.upload_location),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_logo',
            field=models.ImageField(blank=True, null=True, upload_to=stad.models.upload_location),
        ),
    ]
