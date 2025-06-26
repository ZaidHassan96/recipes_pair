



class Recipe():

    def __init__(self, id, name, avg_time, rating):
        self.id = id
        self.name = name
        self.avg_time = avg_time
        self.rating = rating
        
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Recipe({self.id}, {self.name}, {self.avg_time}, {self.rating})"