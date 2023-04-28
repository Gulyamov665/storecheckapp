# Generated by Django 4.1.7 on 2023-04-22 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_alter_united_detail_alter_united_percent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='detail',
            new_name='detail_name',
        ),
        migrations.AlterField(
            model_name='united',
            name='detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.details'),
        ),
    ]