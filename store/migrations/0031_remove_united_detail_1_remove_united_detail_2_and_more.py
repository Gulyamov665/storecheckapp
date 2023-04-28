# Generated by Django 4.1.7 on 2023-04-20 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_united_detail_1_united_detail_2_united_detail_3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='united',
            name='detail_1',
        ),
        migrations.RemoveField(
            model_name='united',
            name='detail_2',
        ),
        migrations.RemoveField(
            model_name='united',
            name='detail_3',
        ),
        migrations.RemoveField(
            model_name='united',
            name='percent_1',
        ),
        migrations.RemoveField(
            model_name='united',
            name='percent_2',
        ),
        migrations.RemoveField(
            model_name='united',
            name='percent_3',
        ),
        migrations.AlterField(
            model_name='united',
            name='percent',
            field=models.CharField(choices=[('0%', '0%'), ('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%')], max_length=20, null=True),
        ),
    ]