# Generated by Django 3.0.5 on 2020-05-09 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersProfile', '0007_auto_20200509_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
        migrations.AddField(
            model_name='child',
            name='photo_main',
            field=models.ImageField(default='dfdfdf', upload_to='photos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='child',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='male', max_length=20),
        ),
    ]