# Generated by Django 3.0 on 2019-12-27 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20191226_1441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['created_date']},
        ),
    ]
