from datetime import date
from APP.models import Movie, Actor, Director, MovieActor

def seed_trending_2024():
    # Clear duplicates (optional safety)
    # Movie.objects.all().delete()
    # Actor.objects.all().delete()
    # Director.objects.all().delete()
    # MovieActor.objects.all().delete()

    # ========== 1. DUNE: PART TWO ==========
    director_dune, _ = Director.objects.get_or_create(
        name="Denis Villeneuve",
        nationality="Canadian",
        country="Canada",
        continent="North America"
    )

    dune = Movie.objects.create(
        title="Dune: Part Two",
        release_date=date(2024, 3, 1),
        duration="2h 46m",
        rating=8.5,
        language="English",
        country="United States",
        genre="Science Fiction, Adventure, Drama",
        description="Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family.",
        director=director_dune
    )

    dune_cast = [
        ("Timothée Chalamet", "American-French", "United States / France", "North America / Europe", "Paul Atreides", "Protagonist"),
        ("Zendaya", "American", "United States", "North America", "Chani", "Love interest / Fremen warrior"),
        ("Rebecca Ferguson", "Swedish", "Sweden", "Europe", "Lady Jessica", "Bene Gesserit / Mother"),
        ("Javier Bardem", "Spanish", "Spain", "Europe", "Stilgar", "Fremen leader"),
        ("Austin Butler", "American", "United States", "North America", "Feyd-Rautha", "Antagonist"),
        ("Florence Pugh", "British", "United Kingdom", "Europe", "Princess Irulan", "Royalty / Narrator"),
        ("Josh Brolin", "American", "United States", "North America", "Gurney Halleck", "Mentor / Warrior"),
    ]
    for name, nat, country, cont, role, char in dune_cast:
        actor, _ = Actor.objects.get_or_create(name=name, nationality=nat, country=country, continent=cont)
        MovieActor.objects.create(movie=dune, actor=actor, role=role, character=char)


    # ========== 2. DEADPOOL & WOLVERINE ==========
    director_dpw, _ = Director.objects.get_or_create(
        name="Shawn Levy",
        nationality="Canadian-American",
        country="Canada / United States",
        continent="North America"
    )

    dpw = Movie.objects.create(
        title="Deadpool & Wolverine",
        release_date=date(2024, 7, 26),
        duration="2h 7m",
        rating=7.9,
        language="English",
        country="United States",
        genre="Action, Comedy, Superhero",
        description="Deadpool recruits Wolverine for a multiverse mission after the TVA threatens to erase him from existence.",
        director=director_dpw
    )

    dpw_cast = [
        ("Ryan Reynolds", "Canadian-American", "Canada / United States", "North America", "Wade Wilson", "Deadpool"),
        ("Hugh Jackman", "Australian", "Australia", "Oceania", "Logan", "Wolverine"),
        ("Emma Corrin", "British", "United Kingdom", "Europe", "Cassandra Nova", "Villain / Antagonist"),
        ("Matthew Macfadyen", "British", "United Kingdom", "Europe", "Paradox", "TVA Agent"),
        ("Morena Baccarin", "Brazilian-American", "Brazil / United States", "South America / North America", "Vanessa", "Love Interest"),
    ]
    for name, nat, country, cont, role, char in dpw_cast:
        actor, _ = Actor.objects.get_or_create(name=name, nationality=nat, country=country, continent=cont)
        MovieActor.objects.create(movie=dpw, actor=actor, role=role, character=char)


    # ========== 3. INSIDE OUT 2 ==========
    director_io2, _ = Director.objects.get_or_create(
        name="Kelsey Mann",
        nationality="American",
        country="United States",
        continent="North America"
    )

    io2 = Movie.objects.create(
        title="Inside Out 2",
        release_date=date(2024, 6, 14),
        duration="1h 36m",
        rating=7.8,
        language="English",
        country="United States",
        genre="Animation, Family, Adventure",
        description="As Riley enters her teenage years, new emotions like Anxiety and Envy join Joy, Sadness, and the old gang in her mind.",
        director=director_io2
    )

    io2_cast = [
        ("Amy Poehler", "American", "United States", "North America", "Joy", "Main Emotion"),
        ("Phyllis Smith", "American", "United States", "North America", "Sadness", "Emotion"),
        ("Lewis Black", "American", "United States", "North America", "Anger", "Emotion"),
        ("Maya Hawke", "American", "United States", "North America", "Anxiety", "New Emotion"),
        ("Ayo Edebiri", "American", "United States", "North America", "Envy", "New Emotion"),
        ("Liza Lapira", "American", "United States", "North America", "Disgust", "Emotion"),
        ("Tony Hale", "American", "United States", "North America", "Fear", "Emotion"),
    ]
    for name, nat, country, cont, role, char in io2_cast:
        actor, _ = Actor.objects.get_or_create(name=name, nationality=nat, country=country, continent=cont)
        MovieActor.objects.create(movie=io2, actor=actor, role=role, character=char)


    # ========== 4. ATLAS ==========
    director_atlas, _ = Director.objects.get_or_create(
        name="Brad Peyton",
        nationality="Canadian",
        country="Canada",
        continent="North America"
    )

    atlas = Movie.objects.create(
        title="Atlas",
        release_date=date(2024, 5, 24),
        duration="2h 0m",
        rating=5.6,
        language="English",
        country="United States",
        genre="Science Fiction, Action, Thriller",
        description="A data analyst must overcome her distrust of AI after being forced to team up with a robot soldier to save humanity.",
        director=director_atlas
    )

    atlas_cast = [
        ("Jennifer Lopez", "American", "United States", "North America", "Atlas Shepherd", "Lead / Analyst"),
        ("Simu Liu", "Canadian", "Canada", "North America", "Harlan", "Antagonist"),
        ("Sterling K. Brown", "American", "United States", "North America", "Colonel Elias Banks", "Supporting"),
        ("Mark Strong", "British", "United Kingdom", "Europe", "General Boothe", "Supporting"),
    ]
    for name, nat, country, cont, role, char in atlas_cast:
        actor, _ = Actor.objects.get_or_create(name=name, nationality=nat, country=country, continent=cont)
        MovieActor.objects.create(movie=atlas, actor=actor, role=role, character=char)


    # ========== 5. WICKED: PART ONE ==========
    director_wicked, _ = Director.objects.get_or_create(
        name="Jon M. Chu",
        nationality="American",
        country="United States",
        continent="North America"
    )

    wicked = Movie.objects.create(
        title="Wicked: Part One",
        release_date=date(2024, 11, 22),
        duration="2h 45m",
        rating=8.0,
        language="English",
        country="United States",
        genre="Musical, Fantasy, Drama",
        description="The story of Elphaba, the misunderstood green-skinned woman who becomes the Wicked Witch of the West.",
        director=director_wicked
    )

    wicked_cast = [
        ("Cynthia Erivo", "British", "United Kingdom", "Europe", "Elphaba Thropp", "Protagonist"),
        ("Ariana Grande", "American", "United States", "North America", "Glinda Upland", "Good Witch"),
        ("Jonathan Bailey", "British", "United Kingdom", "Europe", "Fiyero Tigelaar", "Love Interest"),
        ("Michelle Yeoh", "Malaysian", "Malaysia", "Asia", "Madame Morrible", "Antagonist / Headmistress"),
        ("Jeff Goldblum", "American", "United States", "North America", "The Wizard", "Supporting"),
    ]
    for name, nat, country, cont, role, char in wicked_cast:
        actor, _ = Actor.objects.get_or_create(name=name, nationality=nat, country=country, continent=cont)
        MovieActor.objects.create(movie=wicked, actor=actor, role=role, character=char)

    print("✅ All 2024 trending movies successfully seeded!")