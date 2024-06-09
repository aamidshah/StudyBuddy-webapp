
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Room
from .serializers import RoomSerializer
# create api 


@api_view(['GET'])
def getRoutes(request):
  routes = [
    'GET /api',
    'GET /api/rooms',
    'GET /api/rooms/:id'
  ]
  return Response(routes)



@api_view(['GET'])
def getRooms(request):
  rooms= Room.objects.all()
  seralizer = RoomSerializer(rooms, many=True)
  return Response(seralizer.data)


@api_view(['GET'])
def getRoom(request,pk):
  room= Room.objects.get(id=pk)
  seralizer = RoomSerializer(room, many=False)
  return Response(seralizer.data)