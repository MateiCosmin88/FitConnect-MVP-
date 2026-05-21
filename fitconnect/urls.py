from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from events import views as event_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('accounts/register/', event_views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
