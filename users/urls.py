from django.urls import path

from users import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out')
]