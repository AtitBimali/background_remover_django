# Generated by Django 4.0.6 on 2022-08-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_course_author_remove_course_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
    ]