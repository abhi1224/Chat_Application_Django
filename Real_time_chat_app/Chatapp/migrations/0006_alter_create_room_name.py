# Generated by Django 3.2.7 on 2022-05-14 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatapp', '0005_rename_room_name_create_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_room',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]
