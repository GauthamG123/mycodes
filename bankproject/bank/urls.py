from . import views
from django.urls import path

app_name = 'bankapp'
urlpatterns = (
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('apply/', views.apply, name='apply'),
    path('success/', views.success, name='success'),
)