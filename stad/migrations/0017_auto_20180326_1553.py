# Generated by Django 2.0.3 on 2018-03-26 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stad', '0016_auto_20180326_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_status',
            field=models.IntegerField(choices=[(1, 'Coming'), (2, 'Today'), (3, 'Fineshed')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='stadium',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stad.Arena'),
        ),
    ]