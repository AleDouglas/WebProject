import gc
from django.shortcuts import render
#Import VIEWS
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin # new
# Create your views here.
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Post, UpdatePost
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


class ErrorPage(TemplateView):
    template_name = 'error.html'
####Admin SECTION
class AdminPageView(LoginRequiredMixin, ListView):
    login_url = 'errorPage'
    model = Post
    template_name = 'AdminPage/adminPage.html'
    def get_context_data(self, **kwargs):
        context = super(AdminPageView, self).get_context_data(**kwargs)
        user = get_user_model()
        context['userList'] = user.objects.all()[:5]
        context['updateList'] = UpdatePost.objects.order_by('id').reverse()
        return context

class AdminAllPost(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'AdminPage/allview.html'
    login_url = 'errorPage'

class AdminPostView(LoginRequiredMixin, CreateView):
    login_url = 'errorPage'
    model = Post
    template_name = 'AdminPage/adminPostPage.html'
    fields = ['thumbnail','title', 'description', 'text']

class AdminPostDelete(LoginRequiredMixin, DeleteView):
    login_url = 'errorPage'
    model = Post
    template_name = 'AdminPage/post_delete.html'
    success_url = reverse_lazy('AdminPage')

class AdminEditPost(LoginRequiredMixin, UpdateView):
    login_url = 'errorPage'
    model = Post
    template_name = 'AdminPage/post_edit.html'
    fields = ['thumbnail','title', 'description', 'text']
