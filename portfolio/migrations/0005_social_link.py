# Generated by Django 3.1 on 2020-09-09 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='link',
            field=models.CharField(default='#', max_length=50),
        ),
    ]
