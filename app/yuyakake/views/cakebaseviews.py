from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import TemplateView,ListView, CreateView
from django.urls import reverse_lazy

from app.yuyakake.forms import CreateBaseForm
from app.yuyakake.models import CakeBase


class ListarBaseView(UserPassesTestMixin, ListView):
    template_name = 'cake/base/listar.html'
    model = CakeBase

    def test_func(self):
        return self.request.user.is_superuser


class CrearBaseView(UserPassesTestMixin, CreateView):
    model = CakeBase
    template_name = 'cake/base/crear.html'
    form_class = CreateBaseForm
    success_url = reverse_lazy('base_list')

    def test_func(self):
        return self.request.user.is_superuser



