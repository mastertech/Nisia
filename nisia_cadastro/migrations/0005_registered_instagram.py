# Generated by Django 2.2.3 on 2020-02-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nisia_cadastro', '0004_registered_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered',
            name='instagram',
            field=models.CharField(max_length=20, null=True, verbose_name='Instagram'),
        ),
    ]
