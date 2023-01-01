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
import random


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.wins = 0
        self.ties = 0
        self.rounds = 0
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]  
        
    
    def number_of_rounds(self):
    
    def score(self):
        pass

    

        # player.gesture_chosen = input("Choose your gesture. ")
        # print()

#leave options for player to choose from for AI and Human
#give score
#make gesture to instance variable