from django.urls import path
from ManagingUsers import views
from django.contrib.auth.views import LogoutView


app_name = 'ManagingUsers'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('add/login/', views.UserLoginView.as_view(), name='add'),
    path('profile/', views.TokenListView.as_view(), name='profile'),

]
