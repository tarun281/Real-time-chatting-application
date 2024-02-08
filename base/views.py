from django.shortcuts import render, redirect
from django.views import View

from base.models import Room, Chat

class DashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'main/index.html')
        else:
            return redirect('login')

class RoomsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            rooms = Room.objects.all()
            context = {
                'rooms':rooms
            }
            return render(request, 'main/rooms.html', context)
        else:
            return redirect('login')

class RoomDetailView(View):
    def get(self, request, slug):
        if request.user.is_authenticated:
            room = Room.objects.get(slug=slug)
            chat_messages = Chat.objects.filter(room=room)[0:25]
            context = {
                'room':room,
                'chat_messages':chat_messages
            }
            return render(request, 'main/room.html', context)
        else:
            return redirect('login')
