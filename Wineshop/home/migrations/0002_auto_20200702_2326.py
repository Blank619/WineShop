# Generated by Django 3.0.7 on 2020-07-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeritem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registeritem',
            name='Price',
            field=models.IntegerField(),
        ),
    ]
