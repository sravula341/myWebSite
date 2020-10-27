from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('signup',views.signup_view, name = 'signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('homepage', views.homepage, name='homepage'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
    path('', include('myApp.urls')),
]

# path('', include('django.contrib.auth.urls')),
# path('reset_password', views.reset_password, name='reset_password'),
# path('reset_password', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
# path('reset_password_sent', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
# path('reset/<uidb64>/<token>', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),
# path('reset_password_complete', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
