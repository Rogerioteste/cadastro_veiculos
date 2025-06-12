from django.urls import path
from .views import pagina_cadastro
from django.views.generic import TemplateView

urlpatterns = [
    path('cadastro/', pagina_cadastro, name='pagina_cadastro'),
    path('cadastro/sucesso/', TemplateView.as_view(template_name='cadastro_sucesso.html'), name='cadastro_sucesso'),
]
