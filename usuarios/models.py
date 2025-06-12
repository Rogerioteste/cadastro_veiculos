from django.db import models

# Lista de estados brasileiros
ESTADOS_BRASIL = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
]

class CadastroUsuario(models.Model):
    # Credenciais
    login = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=128)

    # Dados pessoais
    nome_completo = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    # Endereço
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADOS_BRASIL)

    # Documentos opcionais
    cnh_frente = models.FileField(upload_to='documentos/', blank=True, null=True)
    cnh_verso = models.FileField(upload_to='documentos/', blank=True, null=True)
    comprovante_endereco = models.FileField(upload_to='documentos/', blank=True, null=True)

    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo


class ConfiguracaoSite(models.Model):
    nome_site = models.CharField(max_length=100, default='Leilão Direto')
    logo = models.ImageField(upload_to='config/', blank=True, null=True)
    banner = models.ImageField(upload_to='config/', blank=True, null=True)
    cor_principal = models.CharField(max_length=7, default='#0d6efd')  # azul padrão Bootstrap
    telefone_contato = models.CharField(max_length=20, blank=True, null=True)
    email_contato = models.EmailField(blank=True, null=True)
    endereco_empresa = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Configuração do Site"
