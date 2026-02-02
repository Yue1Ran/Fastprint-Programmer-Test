from django.urls import path
from . import views

urlpatterns = [
    path('', views.produk_list, name='list'),
    path('tambah/', views.tambah_produk, name='tambah'),
    path('edit/<int:id>/', views.edit_produk, name='edit'),
    path('hapus/<int:id>/', views.hapus_produk, name='hapus'),
]
