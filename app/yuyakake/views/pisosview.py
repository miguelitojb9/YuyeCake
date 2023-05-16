from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from app.yuyakake.forms import CreateMerengueForm, CreatePisosForm
from app.yuyakake.models import CakeLayer


class ListarPisosView(UserPassesTestMixin, ListView):
    template_name = 'cake/pisos/listar.html'
    model = CakeLayer

    def test_func(self):
        return self.request.user.is_superuser


class CrearPisosView(UserPassesTestMixin,CreateView):
    model = CakeLayer
    template_name = 'cake/pisos/crear.html'
    form_class = CreatePisosForm
    success_url = reverse_lazy('pisos_list')

    def test_func(self):
        return self.request.user.is_superuser

