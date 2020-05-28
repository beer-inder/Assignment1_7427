# Generated by Django 3.0.5 on 2020-05-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersProfile', '0013_auto_20200518_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='gender',
            field=models.CharField(choices=[('female', 'FEMALE'), ('male', 'MALE')], default='male', max_length=20),
        ),
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=100)),
                ('activity_name', models.CharField(max_length=500)),
                ('activity_description', models.CharField(max_length=1000)),
                ('activity_DateTime', models.DateField()),
                ('activity_duration', models.IntegerField()),
                ('children_list', models.ManyToManyField(to='usersProfile.child')),
            ],
            options={
                'verbose_name_plural': 'Activity',
            },
        ),
    ]
