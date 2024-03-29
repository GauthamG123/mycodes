from . import views

from django.urls import path
app_name='credential'
urlpatterns = (
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('application/',views.registration_form,name='application')
)