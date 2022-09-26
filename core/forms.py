from django.core.mail import EmailMessage
from django import forms 


class ContatoForm(forms.Form):
    nome = forms.CharField(label='nome')
    email = forms.EmailField(label='email')
    mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nMensagem: {mensagem}\n\n\nSistema de mensagem automático - Alexandre D.'

        mail = EmailMessage(
            'Sistema de E-mail Automático - Contato',
            conteudo,
            email,
            ['alexandredweb@gmail.com'],
        )

        print('POST -> Email Enviado ao sistema')
        mail.send()