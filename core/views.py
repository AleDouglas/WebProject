import gc
from django.shortcuts import render
#Import VIEWS
from django.views.generic import TemplateView, FormView, ListView, DetailView
# Create your views here.
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Post
from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('Index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

    #Se formulário for válido
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    #Se formulário for inválido
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class BlogView(ListView):
    model = Post
    template_name = 'blog_view.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogdetail_view.html'
    context_object_name = 'post_individual'

class AboutMeView(TemplateView):
    template_name = 'sobremim.html'
    