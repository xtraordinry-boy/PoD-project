from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_registration, name='user_registration'),
    path('create-store/', views.store_creation, name='store_creation'),
    path('upload-design/', views.design_upload, name='design_upload'),
    path('get-designs/', views.retrieve_designs, name='retrieve_designs'),
    path('delete-design/', views.delete_design, name='delete_design'),
]

