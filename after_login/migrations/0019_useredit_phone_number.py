# Generated by Django 3.1.7 on 2021-06-19 14:59

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('after_login', '0018_useredit_model_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='useredit',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+41524204242', max_length=128, region=None),
            preserve_default=False,
        ),
    ]