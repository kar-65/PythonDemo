# Generated by Django 4.1.6 on 2023-02-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_doApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dolist',
            name='date',
            field=models.DateField(default='1999-05-15'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dolist',
            name='prior',
            field=models.IntegerField(),
        ),
    ]
