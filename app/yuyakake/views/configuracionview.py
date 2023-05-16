from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from app.yuyakake.forms import CreateCakeForm
from app.yuyakake.models import Cake


class ListarConfiguracionView(UserPassesTestMixin, ListView):
    template_name = 'cake/configuracion/listar.html'
    model = Cake

    def test_func(self):
        return self.request.user.is_superuser


class CrearConfiguracionView(UserPassesTestMixin, CreateView):
    model = Cake
    template_name = 'cake/configuracion/crear.html'
    form_class = CreateCakeForm
    success_url = reverse_lazy('cake_list')

    def test_func(self):
        return self.request.user.is_superuser

