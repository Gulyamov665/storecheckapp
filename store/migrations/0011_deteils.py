# Generated by Django 4.1.7 on 2023-04-15 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_sku_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deteils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=255)),
                ('detail_pro', models.IntegerField()),
            ],
        ),
    ]
