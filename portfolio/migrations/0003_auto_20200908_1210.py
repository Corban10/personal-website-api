# Generated by Django 3.1 on 2020-09-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200830_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon', models.FileField(upload_to='./skill')),
            ],
        ),
        migrations.AlterField(
            model_name='blogpostimage',
            name='image',
            field=models.ImageField(upload_to='./blog'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(upload_to='./project'),
        ),
    ]
