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

<<<<<<< HEAD
# 1 is rock
# 2 is paper
# 3 is scissors 
# 4 is lizard
# 5 is spock

gestures = ["rock", "paper", "scissors", "lizard", "spock"]


class Player:
    def __init__(self):
        self = self

    def gesture(self, gesture):    
        self.gesture1 = "rock"
        self.paper = 2
        self.scissors = 3
        self.lizard = 4
        self.spock = 5

# class Player:
#     def __init__(self):
#         self.rock = "Rock"
#         self.paper = "Paper"
#         self.scissors = "Scissors"
#         self.lizard = "Lizard"
#         self.spock = "Spock"

=======

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0

    
    def getsture_chosen(self, player):
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]  
        player.gesture_chosen = input("Choose your gesture. ")
        print()
>>>>>>> 4761e58d63236eb1b3afe71af564f0914e2b8140
