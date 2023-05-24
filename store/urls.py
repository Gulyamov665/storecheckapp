from django.urls import path

from store import views


urlpatterns = [
    path('home', views.index, name='home'),
    path('test', views.test, name='test'),
    path('percent/', views.create_united, name='create_united'),
    path('create_sku', views.create_sku, name='create_sku'),
    path('create_trade', views.create_trade, name='create_trade'),
    path('create_territory', views.create_territory, name='create_territory'),
    path('create_detail', views.create_detail, name='create_detail'),
    path('create_percentage', views.create_percentage, name='create_percentage'),
    path('edit_sku/<int:pk>', views.edit_sku, name='edit_sku'),
    path('del_sku/<int:pk>', views.del_sku, name='del_sku'),
    
]
