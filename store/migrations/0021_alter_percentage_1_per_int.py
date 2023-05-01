# Generated by Django 4.1.7 on 2023-04-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_percentage_1_per_int'),
    ]

    operations = [
        migrations.AlterField(
            model_name='percentage_1',
            name='per_int',
            field=models.IntegerField(choices=[(10, '10%'), (20, '20%'), (30, '30%')], null=True),
        ),
    ]