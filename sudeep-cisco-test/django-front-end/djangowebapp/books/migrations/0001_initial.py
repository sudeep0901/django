# Generated by Django 3.0 on 2019-12-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='name')),
                ('price', models.IntegerField(verbose_name='price')),
                ('isbn', models.TextField(verbose_name='isbn')),
            ],
        ),
    ]
