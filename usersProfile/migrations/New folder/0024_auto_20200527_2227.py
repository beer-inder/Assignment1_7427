# Generated by Django 3.0.5 on 2020-05-27 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersProfile', '0023_child_child_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='date_of_birth',
            new_name='child_date_of_birth',
        ),
    ]