# Generated by Django 3.1.5 on 2021-01-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoadFilesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='books/covers/'),
        ),
    ]