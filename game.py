from ai import AI
from human import Human


class Game:

    def __init__(self, name) -> None:
        self.player1 = Human("Player")
        self.player2 = AI("Computer")
        
        
    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.game_phase()
        self.display_winner()
        

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!", '\n' "The best of three is the winner!")

    def display_rules(self):
        print("Rock crushes Scissors",'\n' "Scissors cuts Paper", '\n' "Paper covers Rock", '\n' "Rock crushes Lizard", '\n' "Lizard poisons Spock", '\n'
        "Spock smashes Scissors", '\n' "Scissors decapitates Lizard", '\n' "Lizard eats Paper", '\n' "Paper disproves Spock",'\n' "Spock vaporizes Rock")

    def choose_gestures(self):
        self.player1.choose_gesture()
        self.player2.choose_gesture()

    def compare_gestures(self):
        if self.player1.gesture == self.player2.gesture:
                print("It's a tie!")
        elif self.player1.gesture == 'Rock':
            if self.player2.gesture == 'Scissors' or self.player2.gesture == 'Lizard':
                self.player1.score_point()
            else:
                self.player2.score_point
        elif self.player1.gesture == 'Paper':
            if self.player2.gesture == 'Rock' or self.player2.gesture == 'Spock':
                self.player1.score_point()
            else:
                self.player2.score_point()
        elif self.player1.gesture == 'Scissors':
            if self.player2.gesture == 'Paper' or self.player2.gesture == 'Lizard':
                self.player1.score_point()
            else:
                self.player2.score_point()
        elif self.player1.gesture == 'Lizard':
            if self.player2.gesture == 'Spock' or self.player2.gesture == 'Paper':
                self.player1.score_point()
            else:
                self.player2.score_point()
        elif self.player1.gesture == 'Spock':
            if self.player2.gesture == 'Scissors' or self.player2.gesture == 'Rock':
                self.player1.score_point()
            else:
                self.player2.score_point()
                
    
    def game_phase(self):
        round = 1
        while self.player1.score < 2 and self.player2.score < 2:
            print (f'ROUND {round}')
            self.choose_gestures()
            self.compare_gestures()
            round += 1

    def display_winner(self):
        winner = None
        if self.player1.score >= 2:
            winner = self.player1
        else:
            winner = self.player2
        print(f'{winner.name} wins!') 