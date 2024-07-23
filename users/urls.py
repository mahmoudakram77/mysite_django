from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('logout/', views.logout_view , name='logout'),
    path('register/', views.register , name='register'),
    path('record/', views.record , name='record'),
    path('record/<int:pk>/', views.record_detail , name='detail'),
    path('record/create/', views.create_record, name='create-record'),
    path('record/<int:pk>/edit/', views.editRecord, name='edit-record'),
    path('record/<int:pk>/delete/', views.deleteRecord, name='delete-record'),
]
