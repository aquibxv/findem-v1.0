# Generated by Django 2.2 on 2019-05-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20190525_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/'),
        ),
    ]