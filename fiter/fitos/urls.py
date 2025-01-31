from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('survey/', views.survey_view, name='survey'),
    path('', views.home_view, name='home'),
    path('survey/success/', views.survey_success, name='survey_success'),  # Dodaj ten wiersz]
]