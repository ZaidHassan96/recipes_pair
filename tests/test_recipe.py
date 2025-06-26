from lib.recipe import Recipe



def test_recipe_constructor():

    recipe = Recipe(1,'Spaghetti Bolognese', 45, 4.5)
    assert recipe.id == 1
    assert recipe.name == 'Spaghetti Bolognese'
    assert recipe.avg_time == 45
    assert recipe.rating == 4.5



def test_obj_equality():
    recipe_one = Recipe(1,'Spaghetti Bolognese', 45, 4.5)
    recipe_two = Recipe(1,'Spaghetti Bolognese', 45, 4.5)
    assert recipe_one == recipe_two


def test_formatting():
    recipe_one = Recipe(1,'Spaghetti Bolognese', 45, 4.5)
    assert str(recipe_one) == "Recipe(1, Spaghetti Bolognese, 45, 4.5)"