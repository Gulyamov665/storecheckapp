# Generated by Django 4.1.7 on 2023-04-12 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_sku_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sku',
            name='img',
            field=models.FileField(blank=True, default='static/default.png', upload_to='media/%y/%m/%d/'),
        ),
    ]
