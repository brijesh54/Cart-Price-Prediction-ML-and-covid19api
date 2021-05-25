from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('signup&in', views.RegistrationView.as_view(), name='signup&in'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate'),
    path('set-new-password/<uidb64>/<token>', views.SetNewPasswordView.as_view(), name='set-new-password'),
    path('request-reset-email', views.RequestResetEmailView.as_view(),name='request-reset-email'),
    path('', views.HomeView.as_view(), name='home'),
]    