# Generated by Django 3.1.7 on 2021-03-24 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0005_auto_20210324_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prosetting',
            name='author',
        ),
    ]