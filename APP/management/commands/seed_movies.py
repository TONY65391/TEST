from django.core.management.base import BaseCommand
from APP.movie_seed import seed_trending_2024

class Command(BaseCommand):
    help = "Seeds the database with trending 2024 movies"

    def handle(self, *args, **kwargs):
        seed_trending_2024()
        self.stdout.write(self.style.SUCCESS('✅ Trending 2024 movies successfully seeded!'))
