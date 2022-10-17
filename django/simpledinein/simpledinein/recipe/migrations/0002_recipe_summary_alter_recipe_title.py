# Generated by Django 4.1.2 on 2022-10-17 12:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='summary',
            field=models.TextField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
