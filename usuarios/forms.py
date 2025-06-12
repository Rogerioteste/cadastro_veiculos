from django import forms
from django.contrib.auth.hashers import make_password
from .models import CadastroUsuario

class CadastroUsuarioForm(forms.ModelForm):
    senha1 = forms.CharField(
        widget=forms.PasswordInput,
        label="Senha"
    )
    senha2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirmar Senha"
    )

    class Meta:
        model = CadastroUsuario
        exclude = ['senha']  # o campo real da senha não é exibido
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha1 = cleaned_data.get("senha1")
        senha2 = cleaned_data.get("senha2")

        # Verificação básica para campos vazios
        if not senha1 or not senha2:
            raise forms.ValidationError("Preencha e confirme sua senha.")

        # Senhas devem ser iguais
        if senha1 != senha2:
            raise forms.ValidationError("As senhas não coincidem.")

        # Regras de segurança mínimas
        if len(senha1) < 8 or not any(c.isdigit() for c in senha1) or not any(c.isupper() for c in senha1):
            raise forms.ValidationError(
                "A senha deve ter ao menos 8 caracteres, uma letra maiúscula e um número."
            )

        # Criptografar e armazenar a senha no campo final
        cleaned_data['senha'] = make_password(senha1)
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.senha = self.cleaned_data['senha']  # aplica a senha criptografada
        if commit:
            instance.save()
        return instance
