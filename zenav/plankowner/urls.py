from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from plankowner import views

urlpatterns = [
    path('devices/', views.DeviceList.as_view()),
    path('devices/<int:pk>/', views.DeviceDetail.as_view()),
    path('drivers/', views.DriverList.as_view()),
    path('drivers/<int:pk>/', views.DriverDetail.as_view()),
    path('talents/', views.TalentList.as_view()),
    path('talents/<int:pk>/', views.TalentDetail.as_view()),
    path('watchdog/<int:pk>/', views.watchdog),
    path('panel/<int:pk>', views.view_panel),
]

urlpatterns = format_suffix_patterns(urlpatterns)
