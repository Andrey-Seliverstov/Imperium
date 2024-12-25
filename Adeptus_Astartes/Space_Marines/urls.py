from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>', views.order, name='order'),
    path('create-order/', views.create_order, name='create-order'),
    path('update-order/<int:pk>', views.update_order, name='update-order'),
    path('delete-order/<int:pk>', views.delete_order, name='delete-order'),
]
