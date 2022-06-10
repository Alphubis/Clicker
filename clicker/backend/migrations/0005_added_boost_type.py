# Generated by Django 4.0.4 on 2022-06-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_core_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'casual'), (1, 'auto')], default=0),
        ),
        migrations.AddField(
            model_name='core',
            name='auto_click_power',
            field=models.IntegerField(default=0),
        ),
    ]
