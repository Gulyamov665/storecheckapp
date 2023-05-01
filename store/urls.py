from django.urls import path
from store import views

urlpatterns = [
    path('home/', views.index, name='home'),
    # path('home/', views.create_united, name='home'),
    path('create/', views.create_territory, name='create'),
    path('create_trade/', views.create_trade, name='create_trade'),
    path('create_sku/', views.create_sku, name='create_sku'),
    path('create_detail/', views.create_detail, name='create_detail'),
    path('edit_sku/<int:pk>', views.edit_sku, name='edit_sku'),
    path('del_sku/<int:pk>', views.del_sku, name='del_sku'),
    path('edit_detail/<int:pk>', views.edit_detail, name='edit_detail'),
    path('del_detail/<int:pk>', views.del_detail, name='del_detail'),
    # path('home/', views.index, name='home'),
]
