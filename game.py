from ai import AI
from human import Human


class Game:

 def __init__(self, name) -> None:
        self.human = Human("Player")
        self.ai = AI("Computer")
        
        
def run_game(self):
    self.display_welcome()
    self.display_rules()
    self.game_phase()
    self.number_of_rounds()
    self.return_score()
    self.display_winner()

def display_welcome(self):
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!" "n/" "The best of three is the winner!")

def display_rules(self):
    print("Rock crushes Scissors",'\n' "Scissors cuts Paper", '\n' "Paper covers Rock", '\n' "Rock crushes Lizard", '\n' "Lizard poisons Spock", '\n'
    "Spock smashes Scissors", '\n' "Scissors decapitates Lizard", '\n' "Lizard eats Paper", '\n' "Paper disproves Spock",'\n' "Spock vaporizes Rock")

    
def game_phase(self):
    while self.rounds <= 3:
        if self.human == self.ai:
         print("It's a tie!")
        elif (self.human == '1' and self.ai == '3'):
            self.human.score = +1
            print("You won!")
        elif (self.human == '3' and self.ai == '2'):
            self.human.score = +1
            print("You won!")
        elif (self.human == '2' and self.ai == '1') or (self.human == '1' and self.ai == '4'):
            self.human.score = +1
            print("You won!")
        elif (self.human == '4' and self.ai == '5') or (self.human == '5' and self.ai == '3'):
            self.human.score = +1
            print("You won!")
        elif (self.human == '3' and self.ai == '4') or (self.human == '4' and self.ai == '2'):
            self.human.score = +1
            print("You won!")
        elif(self.human == '2' and self.ai == '5') or (self.human == '5' and self.ai == '1'):
            self.human.score = +1
        print("You won!")
    else:
        print("Computer won!")
        self.ai.score = +1

def number_of_rounds(self):
    while True:
        if self.rounds == 3:
            break
     
def return_score(self):
    return self.score

def display_winner(self):
    if self.human.score == self.ai.score:
        print ("You tied!")
    elif self.human.score > self.ai.score:
        print(f"Congratulations, {self.name.human}! You won!")
    else:
        print(f"{self.ai.name} won!")