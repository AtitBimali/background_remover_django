# Generated by Django 4.0.6 on 2022-08-12 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
