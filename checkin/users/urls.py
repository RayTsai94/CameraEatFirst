from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkin_index, name='checkin_index'),
    path('new/', views.new_checkin, name='new_checkin'),
    path('calendar/', views.calendar_view, name='calendar_view'),
    path('form/', views.checkin_form, name='checkin_form'),
    path('edit/<int:checkin_id>/', views.edit_checkin, name='edit_checkin'),
    path('delete/<int:checkin_id>/', views.delete_checkin, name='delete_checkin'),
] 