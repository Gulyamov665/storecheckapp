# Generated by Django 4.1.7 on 2023-04-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_visit_visit_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('territory_name', models.CharField(max_length=255)),
            ],
        ),
    ]