from django.test import TestCase
from board.models import Board
from django.utils import timezone


class BoardTestCase(TestCase):
    def test_board(self):
        Board.objects.create(title="title", content="content", created_at=timezone.now())
        Board.objects.create(title="title2", content="content2", created_at=timezone.now())
        Board.objects.create(title="title3", content="content3", created_at=timezone.now())

        self.client.get("/board/")

        self.assertEqual(Board.objects.count(), 3)
