from django.contrib.auth import views as auth_views
from django.urls import path, include

from app.customUser.views import SignUpView, MyLoginView, MyRedirectView, AdminDashBoard

urlpatterns = [
    # otras URL de la aplicación
    path('login/', MyLoginView.as_view(), name='login'),
    path('login-redirect/', MyRedirectView.as_view(), name='login_redirect'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('admin-yuya_cake/', AdminDashBoard.as_view(), name='admin_yuyacake'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
