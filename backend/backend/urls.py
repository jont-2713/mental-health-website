from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mentalHealth.urls')),
    path('events/', include('events.urls')),
]
