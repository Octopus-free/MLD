from django.urls import path
from . import views

app_name = 'dbcreate'

urlpatterns = [
    path('', views.IndexFormView.as_view(), name='index'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('db/', views.DBKnowledgeListView.as_view(), name='db_knowledge'),
    path('add/', views.AddInfo.as_view(), name='add_info')
]