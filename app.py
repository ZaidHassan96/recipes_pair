from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.recipe_repository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

recipes_repository = RecipeRepository(connection)
recipes = recipes_repository.all()

# List them out
for recipe in recipes:
    print(recipe)
