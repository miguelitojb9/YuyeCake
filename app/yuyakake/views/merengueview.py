from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from app.yuyakake.forms import CreateMerengueForm
from app.yuyakake.models import CakeMeringue


class ListarMerengueView(UserPassesTestMixin, ListView):
    template_name = 'cake/merengue/listar.html'
    model = CakeMeringue

    def test_func(self):
        return self.request.user.is_superuser


class CrearMerengueView(UserPassesTestMixin,CreateView):
    model = CakeMeringue
    template_name = 'cake/merengue/crear.html'
    form_class = CreateMerengueForm
    success_url = reverse_lazy('merengue_list')

    def test_func(self):
        return self.request.user.is_superuser



