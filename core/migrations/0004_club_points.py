# Generated by Django 2.1.4 on 2019-04-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190408_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='points',
            field=models.IntegerField(default=1),
        ),
    ]
