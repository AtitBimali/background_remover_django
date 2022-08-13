# Generated by Django 4.0.6 on 2022-08-12 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_document_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
