from django.urls import path
from board.views import BoardListAPI

urlpatterns = [
    path("", BoardListAPI.as_view(), name="board_list"),
]
