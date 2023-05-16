"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

from .views.cakesizeview import ListarCakeSizeView, CrearCakeSizeView
from .views.configuracionview import ListarConfiguracionView, CrearConfiguracionView
from .views.merengueview import ListarMerengueView, CrearMerengueView
from .views.pisosview import ListarPisosView, CrearPisosView
from .views.views import *
from .views.cakebaseviews import ListarBaseView, CrearBaseView

urlpatterns = [
    path('new-order/', CreateOrder.as_view(), name='new_order'),

    # Capas
    path('base_list/', ListarBaseView.as_view(), name='base_list'),
    path('base_new/', CrearBaseView.as_view(), name='base_new'),

    # Size
    path('size_list/', ListarCakeSizeView.as_view(), name='size_list'),
    path('size_new/', CrearCakeSizeView.as_view(), name='size_new'),

    # Merengue
    path('merengue_list/', ListarMerengueView.as_view(), name='merengue_list'),
    path('merengue_new/', CrearMerengueView.as_view(), name='merengue_new'),

    # Pisos
    path('pisos_list/', ListarPisosView.as_view(), name='pisos_list'),
    path('pisos_new/', CrearPisosView.as_view(), name='pisos_new'),

    # Cake
    path('cake_list/', ListarConfiguracionView.as_view(), name='cake_list'),
    path('cake_new/', CrearConfiguracionView.as_view(), name='cake_new'),

    # Cargar partes
    path('load_merengue/', cargar_merengue, name='load_merengue'),
    path('load_size/', cargar_size, name='load_size'),
    path('cargar_base/', cargar_base, name='cargar_base'),
    path('cargar_pisos/', cargar_pisos, name='cargar_pisos'),

    # Get Partes
    path('get_merengue/', get_merengue, name='get_merengue'),
    path('get_base/', get_base, name='get_base'),
    path('get_pisos/', get_pisos, name='get_pisos'),
    path('get_size/', get_size, name='get_size'),

    # get muestra pastel
    path('get_cake_sample/', get_cake_sample_ajax, name='get_cake_sample'),
    path('get_cakesamples/', get_cakesamples, name='get_cakesamples'),

]
