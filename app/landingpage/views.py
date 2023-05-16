from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = 'landing.html'