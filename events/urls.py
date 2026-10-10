from django.urls import path


from . import views


app_name = 'events'

urlpatterns = [

path('', views.events_view_list, name='events_list'),
path('<int:event_id>/', views.events_detail, name = 'events_detail'),
path('create/', views.events_create, name='events_create' ),
path('update/<int:event_id>/', views.events_update, name='events_update'),
path('delete/<int:event_id>/', views.events_delete, name='events_delete'),
path('feedback/', views.contact, name='events_feedback'),


]