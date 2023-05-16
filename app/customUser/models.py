from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse
from settings import settings
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=[('G', 'Grato'), ('N', 'No grato')], default='G')
    has_pending_order = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def send_verification_email(self, request):
        uid = urlsafe_base64_encode(force_bytes(self.user.pk)).decode()
        token = default_token_generator.make_token(self.user)
        activation_url = request.build_absolute_uri(reverse('activate', kwargs={'uidb64': uid, 'token': token}))

        html_message = render_to_string('registration/account_activation_email.html', {
            'first_name': self.first_name,
            'activation_url': activation_url,
        })
        plain_message = strip_tags(html_message)

        send_mail(
            'Por favor active su cuenta',
            plain_message,
            settings.EMAIL_FROM,
            [self.user.email],
            html_message=html_message,
        )