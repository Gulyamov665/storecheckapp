# Generated by Django 4.1.7 on 2023-04-17 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_sku_sku_int'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='visit_date',
        ),
    ]
