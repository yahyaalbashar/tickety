# Generated by Django 2.0.3 on 2018-03-26 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stad', '0011_remove_arena_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='weather',
            field=models.CharField(choices=[('Sunny', 'Sunny'), ('Cloudy', 'Cloudy'), ('Rainy', 'Rainy')], max_length=250, null=True),
        ),
    ]
