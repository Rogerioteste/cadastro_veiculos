from django.contrib import admin
from .models import CadastroUsuario, ConfiguracaoSite
from django.utils.html import format_html

@admin.register(CadastroUsuario)
class CadastroUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'telefone', 'email', 'documentos_enviados', 'data_envio')
    search_fields = ('nome_completo', 'cpf', 'email')
    list_filter = ('data_envio',)

    def documentos_enviados(self, obj):
        status = []
        if obj.cnh_frente:
            status.append("CNH Frente")
        if obj.cnh_verso:
            status.append("CNH Verso")
        if obj.comprovante_endereco:
            status.append("Comprovante")
        if status:
            return " / ".join(status)
        return "Nenhum"
    documentos_enviados.short_description = "Documentos"


@admin.register(ConfiguracaoSite)
class ConfiguracaoSiteAdmin(admin.ModelAdmin):
    list_display = ('nome_site', 'telefone_contato', 'email_contato', 'endereco_empresa')
