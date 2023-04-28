# Generated by Django 4.1.7 on 2023-04-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_alter_united_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='united',
            name='percent',
            field=models.CharField(choices=[('10%', '10%'), ('20%', '20%'), ('30%', '30%'), ('40%', '40%'), ('50%', '50%'), ('60%', '60%'), ('70%', '70%'), ('80%', '80%'), ('90%', '90%'), ('100%', '100%'), ('0%', '0%')], default='0%', max_length=20, null=True),
        ),
    ]
