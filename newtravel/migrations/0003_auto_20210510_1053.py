# Generated by Django 3.2.1 on 2021-05-10 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newtravel', '0002_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='Date',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='Phoneno',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
