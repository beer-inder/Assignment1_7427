# Generated by Django 3.0.5 on 2020-05-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersProfile', '0002_auto_20200504_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='email',
            field=models.EmailField(default='something@company.com', max_length=254),
            preserve_default=False,
        ),
    ]