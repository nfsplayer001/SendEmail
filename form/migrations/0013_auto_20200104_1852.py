# Generated by Django 2.2 on 2020-01-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0012_form_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='image',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
