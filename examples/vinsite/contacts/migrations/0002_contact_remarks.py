# Generated by Django 2.1 on 2018-11-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='remarks',
            field=models.CharField(default='test', max_length=250),
            preserve_default=False,
        ),
    ]