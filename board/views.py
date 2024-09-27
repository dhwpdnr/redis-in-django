from rest_framework import generics
from .serializers import BoardSerializer
from .models import Board


class BoardListAPI(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
