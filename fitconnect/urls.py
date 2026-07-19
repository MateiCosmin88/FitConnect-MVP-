from django.contrib import admin
from django.urls import include, path

from events import views as events_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('events/', include('events.urls')),
    path('dashboard/', events_views.dashboard, name='dashboard'),
    path('', include('accounts.urls')),
]
