# Generated by Django 4.2 on 2023-04-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='Created_At',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
