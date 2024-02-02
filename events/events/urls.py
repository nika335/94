
from django.contrib import admin
from django.urls import path
from events_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('events/<str:TITLE>', views.event_detals),
    path('add_events/', views.add_events),
]
