# Generated by Django 3.1.7 on 2021-03-24 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_post_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('headphoto', models.ImageField(default='defo', upload_to='images/')),
                ('prophoto', models.ImageField(default='defo', upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='defo', upload_to='images/'),
        ),
    ]