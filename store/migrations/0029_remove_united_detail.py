# Generated by Django 4.1.7 on 2023-05-18 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_visit_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='united',
            name='detail',
        ),
    ]