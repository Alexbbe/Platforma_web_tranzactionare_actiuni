# Generated by Django 3.2 on 2021-04-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('after_login', '0014_alter_transactions_actual_invested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='actual_invested',
            field=models.FloatField(),
        ),
    ]
