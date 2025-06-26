from lib.recipe import *


class RecipeRepository():

    def __init__(self, connection):
        self.connection = connection

    
    def all(self):

        rows = self.connection.execute("SELECT * FROM recipes")

        recipes = []

        for row in rows:
            recipe = Recipe(row["id"], row["name"], row["avg_time"], row["rating"])
            recipes.append(recipe)
        

        return recipes
    

    def find(self, id):

        row = self.connection.execute("SELECT * FROM recipes WHERE id = %s", [id])[0]

        return Recipe(row["id"], row["name"], row["avg_time"], row["rating"])
