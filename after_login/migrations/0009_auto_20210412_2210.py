# Generated by Django 3.1.7 on 2021-04-12 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('after_login', '0008_auto_20210411_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useredit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
