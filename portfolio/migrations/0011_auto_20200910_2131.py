# Generated by Django 3.1 on 2020-09-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20200909_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='github',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='link',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='social',
            name='link',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='social',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
