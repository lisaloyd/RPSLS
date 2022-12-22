from player import Player


class AI(Player):
    def __init__(self, name):
        super(). __init__()
        self.name = name
        self.score = 0

    def display_choices(self):
        self.display_choices = str(random.randint(1,5))
        
   
#sleep