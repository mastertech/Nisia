# Generated by Django 2.2.3 on 2019-07-16 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nisia_cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered',
            name='registered_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Cadastro efetuado'),
            preserve_default=False,
        ),
    ]