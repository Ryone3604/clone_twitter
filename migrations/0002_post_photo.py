# Generated by Django 3.1.7 on 2021-03-23 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='defo', upload_to='documents/'),
        ),
    ]
