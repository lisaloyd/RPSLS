from player import Player
import random

class AI(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        

    def computer_choice(self):
        self.computer_choice = random.randint(0, 4)
        gesture = self.gesture_list
        print (f"{self.name} picked {gesture[int(self.computer_choice)]}")
#sleep






# user_input = input("Enter your choice by the number (rock[1], paper[2], scissors[3], Lizard [4], Spock[5]): ")