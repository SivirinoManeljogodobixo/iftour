# Generated by Django 3.2.8 on 2023-01-31 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='img_360',
            field=models.ImageField(null=True, upload_to='360/'),
        ),
    ]
