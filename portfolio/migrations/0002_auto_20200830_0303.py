# Generated by Django 3.1 on 2020-08-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.BinaryField(default=b'123'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.BinaryField(default=b'123'),
        ),
    ]
