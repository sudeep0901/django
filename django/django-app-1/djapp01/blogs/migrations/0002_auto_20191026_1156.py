# Generated by Django 2.2.5 on 2019-10-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='details',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='detail_element',
            field=models.CharField(choices=[('h1', 'Header'), ('h2', 'Header 2'), ('h3', 'Header 3'), ('h4', 'Header 4'), ('h5', 'Header 5'), ('h6', 'Header 6'), ('p', 'Paragraph'), ('ul', 'UnorderedLine'), ('ol', 'OrderedLine'), ('img', 'Images'), ('a', 'Anchor'), ('br', 'LineBreak'), ('code', 'code'), ('content', 'content')], max_length=100),
        ),
    ]
