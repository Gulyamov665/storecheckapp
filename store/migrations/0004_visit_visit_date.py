# Generated by Django 4.1.7 on 2023-04-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_visit_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='visit_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]