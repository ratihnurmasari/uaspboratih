# Generated by Django 4.1.2 on 2022-10-30 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seafoodapp', '0007_alter_seafood_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seafood',
            name='image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]