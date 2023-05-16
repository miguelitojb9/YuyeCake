from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy

from app.yuyakake.forms import CreateBaseForm, CreateCakeSizeForm
from app.yuyakake.models import CakeSize


class ListarCakeSizeView(UserPassesTestMixin, ListView):
    template_name = 'cake/size/listar.html'
    model = CakeSize

    def test_func(self):
        return self.request.user.is_superuser


class CrearCakeSizeView(UserPassesTestMixin, CreateView):
    model = CakeSize
    template_name = 'cake/size/crear.html'
    form_class = CreateCakeSizeForm
    success_url = reverse_lazy('size_list')

    def test_func(self):
        return self.request.user.is_superuser





