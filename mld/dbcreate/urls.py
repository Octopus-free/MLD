from django.urls import path
from . import views

app_name = 'dbcreate'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('db/', views.db_knowledge, name='db_knowledge')
]