# Generated by Django 3.0.5 on 2020-05-03 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='guardian_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guardian', to='usersProfile.guardian'),
        ),
    ]