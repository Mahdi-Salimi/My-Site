from django.urls import path
from accounts import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name= 'login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    # path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]