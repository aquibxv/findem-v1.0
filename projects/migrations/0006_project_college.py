# Generated by Django 2.2 on 2019-05-25 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20190524_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='college',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
