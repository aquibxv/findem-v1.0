# Generated by Django 2.2 on 2019-06-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_auto_20190622_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='project_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
