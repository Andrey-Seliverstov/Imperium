from django.urls import path
from . import views


urlpatterns = [
    path('', views.history, name='history'),
    path('<int:mil_num>', views.detail, name='detail'),
    path('create-record/', views.create_record, name='create-record'),
    path('update-record/<int:mil_num>', views.update_record, name='update-record'),
    path('delete-record/<int:mil_num>', views.delete_record, name='delete-record'),
]
