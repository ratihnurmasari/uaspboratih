# Generated by Django 4.1.2 on 2022-10-31 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seafoodapp', '0015_alter_seafood_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seafood',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/'),
        ),
    ]
