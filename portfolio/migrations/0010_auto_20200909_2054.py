# Generated by Django 3.1 on 2020-09-09 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20200909_2053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='featured',
            new_name='show',
        ),
    ]
