# Generated by Django 3.1.7 on 2021-04-11 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('after_login', '0007_transactions_plm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='plm',
        ),
        migrations.AddField(
            model_name='transactions',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]