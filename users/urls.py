
from django.urls import path
from .views import (
    CustomUserCreate, BlacklistTokenUpdateView, VerifyEmail, LoginAPIView,
    RequestPasswordResetEmail, PasswordTokenCheckAPI, SetNewPasswordAPIView,ResendEmail)

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('signin/', LoginAPIView.as_view(), name="signin"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('resend-email/', ResendEmail.as_view(), name="resend-email"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]
