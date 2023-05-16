from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from .models import Customer
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


class SignUpView(generic.CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return self.success_url



@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@method_decorator(login_required, name='dispatch')
class ProfileView(generic.UpdateView):
    model = Customer
    fields = ['first_name', 'last_name', 'phone_number']
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.customer


def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, '¡Su cuenta ha sido verificada! Ahora puede iniciar sesión.')
        return redirect('login')
    else:
        messages.error(request, 'El enlace de verificación es inválido o ha expirado.')
        return redirect('signup')





class MyLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return '/login-redirect/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:

            login(self.request, user)
            return redirect(self.get_success_url())
        return super().form_invalid(form)

class MyRedirectView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser :
            return redirect('admin_yuyacake')
        else:
            return redirect('landing')


class AdminDashBoard(LoginRequiredMixin, TemplateView):
    template_name = 'admin/dashboard_admin.html'
