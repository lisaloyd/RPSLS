#Rock crushes Scissors
#Scissors cuts Paper 
#Paper covers Rock
#Rock crushes Lizard
#Lizard poisons Spock
#Spock smashes Scissors
#Scissors decapitates Lizard
#Lizard eats Paper
#Paper disproves Spock
#Spock vaporizes Rock


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0

    
    def getsture_chosen(self, player):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]  
        player.gesture_chosen = input("Choose your gesture. ")
        print()