# Generated by Django 4.2.7 on 2023-12-03 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_testimonial_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
