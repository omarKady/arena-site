# Generated by Django 2.1.4 on 2019-04-15 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_matchu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchu',
            name='club_visit',
        ),
        migrations.RemoveField(
            model_name='matchu',
            name='occasio',
        ),
        migrations.DeleteModel(
            name='Matchu',
        ),
    ]