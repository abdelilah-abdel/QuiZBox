# Generated by Django 3.2.13 on 2022-06-28 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_quiz_background'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='background',
        ),
    ]
