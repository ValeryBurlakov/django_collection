from django.contrib.auth.views import LogoutView
from django.urls import path, include

from . import views

from django.conf.urls.static import static
from django.conf import settings
# from ..homework_project import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'logout/', views.logout_view, name='logout'),
    path('get_users/', views.get_users, name='users'),
    path('coin_details/<int:coin_id>/', views.coin_details, name='coin_details'),
    path('create_collection_view/', views.create_collection_view, name='create_collection_view'),
    path('get_coin/', views.get_coin, name='get_coin'),
    path('get_collection/', views.get_collection, name='get_collection'),
    path('add_coin/', views.add_coin, name='add_coin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
