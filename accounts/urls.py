from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetView, PasswordResetDoneView,
                                       PasswordResetConfirmView, PasswordResetCompleteView,
                                       )
from django.urls import path
from accounts.views import profile, SignUpView, ProfileUpdateView

urlpatterns=[
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('pasword-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
]