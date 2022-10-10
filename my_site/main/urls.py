from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('content', views.content, name='content'),
    path('about', views.about, name='about'),
    path('chitka4', views.chitka, name='chitka'),
    path('chitka3', views.chitka3, name='chitka'),
    path('chitka2', views.chitka2, name='chitka'),
    path('create', views.create, name='create'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )