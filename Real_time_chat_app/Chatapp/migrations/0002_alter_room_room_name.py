# Generated by Django 3.2.7 on 2022-05-11 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_name',
            field=models.TextField(max_length=50),
        ),
    ]
