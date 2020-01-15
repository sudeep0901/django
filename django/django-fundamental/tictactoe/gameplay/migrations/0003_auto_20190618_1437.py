# Generated by Django 2.2.2 on 2019-06-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_move_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First Player To Move'), ('S', 'Second Player To Move'), ('W', 'First Player To Wins'), ('L', 'Second Player WINS'), ('D', 'Draw')], default='F', max_length=1),
        ),
        migrations.AlterField(
            model_name='move',
            name='status',
            field=models.CharField(choices=[('F', 'First Player To Move'), ('S', 'Second Player To Move'), ('W', 'First Player To Wins'), ('L', 'Second Player WINS'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]
