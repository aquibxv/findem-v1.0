# Generated by Django 2.2 on 2019-06-30 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_auto_20190630_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinformation',
            name='college_university',
        ),
    ]
