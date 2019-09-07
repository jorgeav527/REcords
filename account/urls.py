from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as account_views

# Account urls 

urlpatterns = [
    # /account/ 
    # basic information
    path('', account_views.home_account_view , name='account-home'), # Main Page
    path('about/', account_views.about_account_view , name='account-about'),
    path('contact/', account_views.contact_account_view, name='account-contact'),
    # CRUD
    path('register/', account_views.register, name='account-register'),
    path('profile/', account_views.profile , name='account-profile'),
    path('profile/<str:username>/', account_views.delete_user , name='account-delete'),
    # log views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # password change
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # password reset
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]