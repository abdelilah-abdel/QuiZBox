# Generated by Django 3.2.13 on 2022-06-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='backgroundimg',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]
