from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import games_view

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('games/', views.games, name='games'),  # Games page
    path('login/', views.login_view, name='login'),  # Login page
    path('games/', games_view, name='games'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)