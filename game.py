from ai import AI
from human import Human


class Game:

 def __init__(self, name) -> None:
        self.human = Human("Player")
        self.ai = AI("Computer")
        self.score = 0
        self.wins = 0
        self.ties = 0

def run_game(self):
    pass

def display_welcome(self):
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!" "n/" "The best of three is the winner!" "n/" 
    "Use the number keys to choose your gesture. ")

def display_rules(self):
    print("Rock crushes Scissors",'\n' "Scissors cuts Paper", '\n' "Paper covers Rock", '\n' "Rock crushes Lizard", '\n' "Lizard poisons Spock", '\n'
    "Spock smashes Scissors", '\n' "Scissors decapitates Lizard", '\n' "Lizard eats Paper", '\n' "Paper disproves Spock",'\n' "Spock vaporizes Rock")

def display_gesture_chosen(self):
    pass
    
def game_phase(self):
    if self.human == self.ai:
         print("It's a tie!")
    elif ((self.human == '1' and self.ai == '3') or (self.human == '3' and self.ai = '2') or
         (self.human == '2' and self.ai == '1') or (self.human == '1' and self.ai == '4') or
         (self.human == '4' and self.ai == '5') or (self.human == '5' and self.ai == '3') or
         (self.human == '3' and self.ai == '4') or (self.human == '4' and self.ai == '2') or
         (self.human == '2' and self.ai == '5') or (self.human == '5' and self.ai == '1')):
        print("You won!") 
    else:
        print("Computer won!")
     
def return_score(self):
    return self.score

def display_winner(self):
    pass
