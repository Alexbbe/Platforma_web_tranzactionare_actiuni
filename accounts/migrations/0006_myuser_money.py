# Generated by Django 3.1.7 on 2021-04-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210321_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='money',
            field=models.BigIntegerField(default=1000000),
            preserve_default=False,
        ),
    ]
