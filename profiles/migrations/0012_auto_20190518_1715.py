# Generated by Django 2.2 on 2019-05-18 11:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20190513_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinformation',
            name='user',
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
