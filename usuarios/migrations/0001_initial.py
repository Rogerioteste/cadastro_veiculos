# Generated by Django 5.2 on 2025-06-05 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50, unique=True)),
                ('senha', models.CharField(max_length=128)),
                ('nome_completo', models.CharField(max_length=120)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(blank=True, max_length=20, null=True)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('cep', models.CharField(max_length=10)),
                ('endereco', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=50, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('cnh_frente', models.FileField(blank=True, null=True, upload_to='documentos/')),
                ('cnh_verso', models.FileField(blank=True, null=True, upload_to='documentos/')),
                ('comprovante_endereco', models.FileField(blank=True, null=True, upload_to='documentos/')),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfiguracaoSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_site', models.CharField(default='Leilão Direto', max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='config/')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='config/')),
                ('cor_principal', models.CharField(default='#0d6efd', max_length=7)),
                ('telefone_contato', models.CharField(blank=True, max_length=20, null=True)),
                ('email_contato', models.EmailField(blank=True, max_length=254, null=True)),
                ('endereco_empresa', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
