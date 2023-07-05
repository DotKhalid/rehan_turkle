# Generated by Django 3.2.16 on 2022-11-09 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('turkle', '0012_auto_20210923_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveProject',
            fields=[
            ],
            options={
                'ordering': ['name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('turkle.project',),
        ),
        migrations.CreateModel(
            name='ActiveUser',
            fields=[
            ],
            options={
                'ordering': ['first_name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
        ),
    ]
