# Generated by Django 3.1.7 on 2021-04-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_myuser_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='money',
            field=models.FloatField(),
        ),
    ]