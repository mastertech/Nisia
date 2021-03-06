# Generated by Django 2.2.3 on 2020-02-20 15:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nisia_cadastro', '0005_registered_instagram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Título')),
                ('date_event', models.DateField(verbose_name='Dia do evento')),
                ('start_time', models.TimeField(verbose_name='Início do evento')),
                ('end_time', models.TimeField(verbose_name='Término do evento')),
                ('adress', models.CharField(max_length=120, verbose_name='Local do evento')),
                ('description', models.TextField(verbose_name='Descrição do evento')),
                ('type_event', models.CharField(choices=[('GRATUITO', 'GRATUITO'), ('PAGO', 'PAGO'), ('TRAGA UMA DOAÇÃO', 'TRAGA UMA DOAÇÃO')], default='Escolher', max_length=50, verbose_name='Tipo do evento?')),
                ('slug', models.CharField(max_length=120, verbose_name='Link de inscrição')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Calendário',
            },
        ),
        migrations.AlterField(
            model_name='registered',
            name='role',
            field=models.CharField(choices=[('A ESTUDANTE', 'A ESTUDANTE'), ('A PROGRAMADORA', 'A PROGRAMADORA'), ('A MENTORA', 'A MENTORA'), ('OS EDUCADORES', 'OS EDUCADORES'), ('A EMPREGADORA', 'A EMPREGADORA'), ('OS FACILITADORES', 'OS FACILITADORES'), ('OS APOIADORES', 'OS APOIADORES')], default='A ESTUDANTE', max_length=50, verbose_name='Com quais perfis você se identifica hoje?'),
        ),
    ]
