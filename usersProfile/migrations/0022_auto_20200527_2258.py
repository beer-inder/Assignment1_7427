# Generated by Django 3.0.5 on 2020-05-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersProfile', '0021_auto_20200527_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='child_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='male', max_length=20),
        ),
    ]
