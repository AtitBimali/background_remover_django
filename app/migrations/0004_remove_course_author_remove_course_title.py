# Generated by Django 4.0.6 on 2022-08-12 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_course_delete_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='author',
        ),
        migrations.RemoveField(
            model_name='course',
            name='title',
        ),
    ]
