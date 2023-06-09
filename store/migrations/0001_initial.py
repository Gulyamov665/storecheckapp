# Generated by Django 4.1.2 on 2023-03-25 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, upload_to='')),
                ('sku_name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.ManyToManyField(blank=True, null=True, to='store.sku')),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Магазин', to='store.trade')),
            ],
        ),
    ]
