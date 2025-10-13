import os
import django

# setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TEST.settings')
django.setup()

from datetime import date
from APP.models import Movie, Actor, Director, MovieActor

# # # 1️⃣ INCEPTION
# nolan, _ = Director.objects.get_or_create(
#     name="Christopher Nolan",
#     nationality="British-American",
#     country="United Kingdom / United States",
#     continent="Europe & North America"
# )

# inception = Movie.objects.create(
#     title="Inception",
#     release_date=date(2010, 7, 16),
#     duration="2h 28m",
#     rating=8.8,
#     language="English",
#     country="United States",
#     genre="Sci-Fi, Action, Thriller",
#     description="A skilled thief who can infiltrate dreams must plant an idea into a target’s mind to earn redemption.",
#     director=nolan,
# )

# actors_data = [
#     ("Leonardo DiCaprio", "American", "United States", "North America", "Dom Cobb", "Extractor / Main Protagonist"),
#     ("Joseph Gordon-Levitt", "American", "United States", "North America", "Arthur", "Cobb’s Partner / Point Man"),
#     ("Elliot Page", "Canadian", "Canada", "North America", "Ariadne", "Architect"),
#     ("Tom Hardy", "British", "United Kingdom", "Europe", "Eames", "Forger"),
#     ("Ken Watanabe", "Japanese", "Japan", "Asia", "Saito", "Businessman / Employer"),
# ]


# for name, nationality, country, continent, role, character in actors_data:
#     actor, _ = Actor.objects.get_or_create(
#         name=name, nationality=nationality, country=country, continent=continent
#     )
#     MovieActor.objects.create(movie=inception, actor=actor, role=role, character=character)

# # 2️⃣ BLACK PANTHER
# coogler, _ = Director.objects.get_or_create(
#     name="Ryan Coogler", nationality="American", country="United States", continent="North America"
# )

# black_panther = Movie.objects.create(
#     title="Black Panther",
#     release_date=date(2018, 2, 16),
#     duration="2h 14m",
#     rating=7.3,
#     language="English (some Xhosa)",
#     country="United States",
#     genre="Action, Adventure, Sci-Fi",
#     description="T’Challa returns to Wakanda to become king, but an old enemy challenges his right to the throne.",
#     director=coogler
# )

# actors_data = [
#     ("Chadwick Boseman", "American", "United States", "North America", "T’Challa / Black Panther", "King of Wakanda"),
#     ("Michael B. Jordan", "American", "United States", "North America", "Erik Killmonger", "Villain / Rival to T’Challa"),
#     ("Lupita Nyong’o", "Kenyan-Mexican", "Kenya / Mexico", "Africa & North America", "Nakia", "Spy / Love Interest"),
#     ("Danai Gurira", "American (Zimbabwean roots)", "United States", "North America", "Okoye", "General of the Dora Milaje"),
#     ("Letitia Wright", "Guyanese-British", "Guyana / United Kingdom", "South America & Europe", "Shuri", "T’Challa’s Sister / Tech Genius"),
# ]

# for name, nationality, country, continent, role, character in actors_data:
#     actor, _ = Actor.objects.get_or_create(name=name, nationality=nationality, country=country, continent=continent)
#     MovieActor.objects.create(movie=black_panther, actor=actor, role=role, character=character)

# # 3️⃣ THE DARK KNIGHT
# dark_knight = Movie.objects.create(
#     title="The Dark Knight",
#     release_date=date(2008, 7, 18),
#     duration="2h 32m",
#     rating=9.0,
#     language="English",
#     country="United States / United Kingdom",
#     genre="Action, Crime, Drama",
#     description="Batman faces chaos as the Joker plunges Gotham into anarchy.",
#     director=nolan
# )

# actors_data = [
#     ("Christian Bale", "British", "United Kingdom", "Europe", "Bruce Wayne / Batman", "Hero / Vigilante"),
#     ("Heath Ledger", "Australian", "Australia", "Oceania", "The Joker", "Antagonist"),
#     ("Aaron Eckhart", "American", "United States", "North America", "Harvey Dent / Two-Face", "District Attorney"),
#     ("Maggie Gyllenhaal", "American", "United States", "North America", "Rachel Dawes", "Love Interest"),
#     ("Gary Oldman", "British", "United Kingdom", "Europe", "James Gordon", "Commissioner / Ally"),
# ]

# for name, nationality, country, continent, role, character in actors_data:
#     actor, _ = Actor.objects.get_or_create(name=name, nationality=nationality, country=country, continent=continent)
#     MovieActor.objects.create(movie=dark_knight, actor=actor, role=role, character=character)


# # 4️⃣ AVATAR: THE WAY OF WATER
# cameron, _ = Director.objects.get_or_create(
#     name="James Cameron", nationality="Canadian", country="Canada", continent="North America"
# )

# avatar = Movie.objects.create(
#     title="Avatar: The Way of Water",
#     release_date=date(2022, 12, 16),
#     duration="3h 12m",
#     rating=7.6,
#     language="English (Na’vi)",
#     country="United States",
#     genre="Adventure, Fantasy, Sci-Fi",
#     description="Jake Sully and Neytiri protect their family from returning human invaders.",
#     director=cameron
# )

# actors_data = [
#     ("Sam Worthington", "British-Australian", "Australia / UK", "Oceania & Europe", "Jake Sully", "Protagonist / Former Marine"),
#     ("Zoe Saldaña", "American", "United States", "North America", "Neytiri", "Na’vi Princess"),
#     ("Sigourney Weaver", "American", "United States", "North America", "Kiri", "Adopted Daughter / Scientist Avatar"),
#     ("Kate Winslet", "British", "United Kingdom", "Europe", "Ronal", "Metkayina Clan Leader"),
#     ("Stephen Lang", "American", "United States", "North America", "Miles Quaritch", "Villain"),
# ]

# for name, nationality, country, continent, role, character in actors_data:
#     actor, _ = Actor.objects.get_or_create(name=name, nationality=nationality, country=country, continent=continent)
#     MovieActor.objects.create(movie=avatar, actor=actor, role=role, character=character)

# # 5️⃣ SPIDER-MAN: NO WAY HOME
# watts, _ = Director.objects.get_or_create(
#     name="Jon Watts", nationality="American", country="United States", continent="North America"
# )

# spiderman = Movie.objects.create(
#     title="Spider-Man: No Way Home",
#     release_date=date(2021, 12, 17),
#     duration="2h 28m",
#     rating=8.2,
#     language="English",
#     country="United States",
#     genre="Action, Adventure, Superhero",
#     description="Peter Parker's identity is revealed, leading to a multiverse collision of Spider-Men and villains.",
#     director=watts
# )

# actors_data = [
#     ("Tom Holland", "British", "United Kingdom", "Europe", "Peter Parker / Spider-Man", "Main Protagonist"),
#     ("Zendaya", "American", "United States", "North America", "MJ", "Girlfriend"),
#     ("Benedict Cumberbatch", "British", "United Kingdom", "Europe", "Doctor Strange", "Mentor / Sorcerer"),
#     ("Jacob Batalon", "Filipino-American", "Philippines / USA", "Asia & North America", "Ned Leeds", "Best Friend"),
#     ("Willem Dafoe", "American", "United States", "North America", "Norman Osborn / Green Goblin", "Villain"),
# ]

# for name, nationality, country, continent, role, character in actors_data:
#     actor = Actor.objects.get_or_create(name=name, nationality=nationality, country=country, continent=continent)
#     # MovieActor.objects.create(movie=spiderman, actor=actor, role=role, character=character)

movie = Movie.objects.get(title='Inception')
actors = movie.actors.all()
print(actors)


print("✅ MovieBox seed data successfully added!")
