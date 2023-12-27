from django.urls import path
from . import views
app_name='todoapp'

urlpatterns = [
    path('',views.add,name='add'),
    path('complete/<int:taskid>/',views.completed,name='complete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetails'),
    path('cbvupdates/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdates'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete'),
]