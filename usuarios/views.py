from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroUsuarioForm
from .models import ConfiguracaoSite

def pagina_cadastro(request):
    config = ConfiguracaoSite.objects.first()  # configurações visuais (logo, cor, etc.)

    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro enviado com sucesso!')
            return redirect('cadastro_sucesso')  # redireciona após cadastro válido
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')

    else:
        form = CadastroUsuarioForm()

    return render(request, 'cadastro.html', {
        'form': form,
        'config': config
    })
