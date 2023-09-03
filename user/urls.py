from django.urls import path
from . import views

urlpatterns = [
    path('refresh-token/', views.refresh_token_view),
    path('registration/', views.registration_view,name='registration'),
    path('login/', views.login_view),
]
