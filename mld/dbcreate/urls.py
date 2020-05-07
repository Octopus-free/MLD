from django.urls import path, include
from . import views
from .api_views import AlgorithmsBookViewSet, MetricsBookViewSet
from rest_framework import routers


app_name = 'dbcreate'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'AlgorithmsBook', AlgorithmsBookViewSet)
router.register(r'MetricsBook', MetricsBookViewSet)

urlpatterns = [
    path('', views.IndexFormView.as_view(), name='index'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('db/', views.DBKnowledgeListView.as_view(), name='db_knowledge'),
    path('add/', views.AddInfo.as_view(), name='add_info'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v0/', include(router.urls)),

]


