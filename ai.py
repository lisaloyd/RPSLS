from player import Player
import random

class AI(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        

    def choose_gesture(self):
        self.gesture = random.choice(self.gesture_list)
        gesture = self.gesture_list
        print (f"{self.name} picked {self.gesture}")
#sleep

    



