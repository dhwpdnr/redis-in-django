from django.core.management.base import BaseCommand
from board.models import Board
from django.utils import timezone
from datetime import timedelta
import random


class Command(BaseCommand):
    help = "This command creates many boards"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many boards do you want to create?"
        )

    def get_random_date_within_10_years(self):
        # 매번 현재 시간 가져오기
        now = timezone.now()

        # 10년(365 * 10일) 이내 랜덤한 날짜 생성
        max_days = 365 * 10
        random_days = random.randint(0, max_days)
        random_date = now - timedelta(days=random_days)

        # 하루(24시간) 이내 랜덤 시간(시, 분, 초) 생성
        random_seconds = random.randint(0, 24 * 60 * 60 - 1)  # 하루의 초 단위 시간
        random_time = timedelta(seconds=random_seconds)

        # 날짜에 랜덤 시간 더하기
        random_datetime = random_date + random_time
        return random_datetime

    def handle(self, *args, **options):
        number = options.get("number")

        for i in range(number):
            random_created_at = self.get_random_date_within_10_years()
            Board.objects.create(title=f"Board{i}", content="hello", created_at=random_created_at)

            # 진행도 출력
            progress = (i + 1) / number * 100
            self.stdout.write(f"\rProgress: {progress:.2f}% ({i + 1}/{number})", ending="")
            self.stdout.flush()

        self.stdout.write(self.style.SUCCESS(f"\n{number} boards created"))