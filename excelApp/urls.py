from django.urls import path
from excelApp import views

urlpatterns = [
    path('export/', views.export_xlsx, name='export'),
]
