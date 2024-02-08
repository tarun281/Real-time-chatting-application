from django.urls import path
from base.views import DashboardView, RoomsView, RoomDetailView

urlpatterns = [
    path('',DashboardView.as_view(), name='dashboard'),
    path('rooms/',RoomsView.as_view(), name='rooms'),
    path('room/<slug:slug>/',RoomDetailView.as_view(), name='room-detail'),
]