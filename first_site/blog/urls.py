from blog import views 
from django.urls import path
app_name = 'first_site'
urlpatterns = [
    path('', views.registered_user),
    path('create_product/', views.create_product),
    path('list_all_products/', views.list_all_products),
    path('add_to_cart/<int:pk>', views.add_to_cart),
    path('delete_cart/', views.delete_cart),
   
]