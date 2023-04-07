# Generated by Django 3.2.13 on 2022-06-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20220625_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='images',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]