# Generated by Django 3.1.7 on 2021-03-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210320_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
