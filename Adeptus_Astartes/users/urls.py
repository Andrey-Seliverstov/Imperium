from django.urls import path
from . import views


urlpatterns = [
    path('', views.personal_account, name='personal-account'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
