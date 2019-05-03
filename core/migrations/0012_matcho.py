# Generated by Django 2.1.4 on 2019-04-15 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190415_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matcho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_date', models.DateTimeField(verbose_name='play date')),
                ('club_visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Club')),
                ('occasio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.League')),
            ],
        ),
    ]