from . import views
from django.urls import path

app_name = 'bankapp'
urlpatterns = (
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('application_form/', views.show_application_form, name='application_form'),
    path('submit_application/', views.submit_application, name='submit_application'),
)
