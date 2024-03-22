from django.urls import path, include

from . import views

from django.conf.urls.static import static
from django.conf import settings
# from ..homework_project import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('get_users/', views.get_users, name='пользователи'),
    path('get_coin/<int:coin_id>/', views.get_coin, name='монета по id'),
    path('add_coin/', views.add_coin, name='add_coin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
