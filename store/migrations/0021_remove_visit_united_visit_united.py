# Generated by Django 4.1.7 on 2023-04-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_remove_details_detail_pro_remove_procentage_choco_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='united',
        ),
        migrations.AddField(
            model_name='visit',
            name='united',
            field=models.ManyToManyField(blank=True, null=True, to='store.united'),
        ),
    ]
