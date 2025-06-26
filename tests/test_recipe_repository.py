from lib.recipe import Recipe
from lib.recipe_repository import *


def test_find_all_method(db_connection):

    db_connection.seed("seeds/recipes.sql")

    repository = RecipeRepository(db_connection)

    recipes = repository.all()

    assert recipes == [
    Recipe(1, 'Spaghetti Bolognese', 45, 4.5),
    Recipe(2, 'Chicken Curry', 60, 4.7),
    Recipe(3, 'Vegetable Stir Fry', 25, 4.2),
    Recipe(4, 'Beef Tacos', 30, 4.6),
    Recipe(5, 'Lemon Cheesecake', 90, 4.9)
]



def test_find_specific(db_connection):

    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(2)

    assert recipe == Recipe(2, 'Chicken Curry', 60, 4.7)
    


