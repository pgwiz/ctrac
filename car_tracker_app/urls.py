from django.urls import path, re_path
from ctrack import settings
from . import views
from django.views import static


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

    # other URL patterns

]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
        re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    ]
