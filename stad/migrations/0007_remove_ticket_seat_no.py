# Generated by Django 2.0.3 on 2018-03-20 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stad', '0006_auto_20180320_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='seat_no',
        ),
    ]
