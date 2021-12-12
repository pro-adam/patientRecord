from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('add-record/', views.add_record,name='add-record'),
    path('update-record/<int:patient_id>/', views.update_record,name='update-record'),
    path('delete-record/<int:id>/', views.delete_record,name='delete-record'),
]
