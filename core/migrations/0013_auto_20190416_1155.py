# Generated by Django 2.1.4 on 2019-04-16 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_matcho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matcho',
            name='club_visit',
        ),
        migrations.RemoveField(
            model_name='matcho',
            name='occasio',
        ),
        migrations.DeleteModel(
            name='Matcho',
        ),
    ]
