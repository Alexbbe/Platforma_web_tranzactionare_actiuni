# Generated by Django 3.2 on 2021-04-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('after_login', '0011_auto_20210413_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='actual_invested',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
