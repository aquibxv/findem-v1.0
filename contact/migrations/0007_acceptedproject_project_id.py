# Generated by Django 2.2 on 2019-06-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20190623_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceptedproject',
            name='project_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
