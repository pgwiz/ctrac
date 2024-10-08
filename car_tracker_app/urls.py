from django.urls import path, re_path
from ctrack import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('track/', views.track, name='track'),
    path('login/', views.login, name='login'),
    path('register_vehicle/', views.register_vehicle, name='register_vehicle'),
    path('manage_vehicles/', views.manage_vehicles, name='manage_vehicles'),
    path('edit_vehicle/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),
    path('delete_vehicle/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
    path('docu/', views.docu, name='docu'),
    path('api/vehicle/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('track_vehicle/<int:vehicle_id>/', views.track_vehicle, name='track_vehicle'),
    path('register/', views.register_view, name='register'),
    path('manage_users/', views.manage_users_view, name='manage_users'),
    path('delete_user/<pk>/', views.delete_user_view, name='delete_user'),

    # other URL patterns

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    application = WhiteNoise(
        application,
        root=settings.STATIC_ROOT,
        prefix=settings.STATIC_URL,
    )
