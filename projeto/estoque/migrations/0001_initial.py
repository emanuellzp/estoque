# Generated by Django 5.0.3 on 2024-11-07 00:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em: ')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em: ')),
                ('nf', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Nota fiscal')),
                ('movimento', models.CharField(choices=[('e', 'entrada'), ('s', 'saída')], max_length=1)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='EstoqueItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('saldo', models.PositiveIntegerField()),
                ('estoque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.estoque')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
