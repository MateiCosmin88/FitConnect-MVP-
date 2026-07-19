from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='list'),
    path('new/', views.event_create, name='create'),
    path('<int:pk>/', views.event_detail, name='detail'),
    path('<int:pk>/edit/', views.event_edit, name='edit'),
    path('<int:pk>/delete/', views.event_delete, name='delete'),
    path('<int:pk>/rsvp/', views.rsvp, name='rsvp'),
    path('<int:pk>/cancel/', views.cancel_rsvp, name='cancel_rsvp'),
    path('<int:pk>/attendees/', views.attendees, name='attendees'),
]
