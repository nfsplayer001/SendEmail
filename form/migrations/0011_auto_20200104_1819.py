# Generated by Django 2.2 on 2020-01-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_auto_20200104_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='email',
            field=models.EmailField(default=None, max_length=123),
        ),
        migrations.AddField(
            model_name='form',
            name='first_name',
            field=models.CharField(default=None, max_length=123),
        ),
        migrations.AddField(
            model_name='form',
            name='last_name',
            field=models.CharField(default=None, max_length=123),
        ),
        migrations.AddField(
            model_name='form',
            name='phone',
            field=models.IntegerField(default=None),
        ),
    ]
