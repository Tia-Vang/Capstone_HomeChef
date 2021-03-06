
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('results/', views.results, name='results'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('recipe/<int:id>/comments', views.comments, name='comments'),
    path('foryou/', views.for_you, name='tailored'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

