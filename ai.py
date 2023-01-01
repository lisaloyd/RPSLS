from player import Player
import random

class AI(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        

    def choose_gesture(self):
        self.choose_gesture = random.randint(0, 4)
        gesture = self.gesture_list
        print (f"{self.name} picked {gesture[int(self.choose_gesture)]}")
#sleep

<<<<<<< HEAD
    
=======
    def return_score(self):
        pass
>>>>>>> 031d53ff3135521867255a711ad5cd289ea171ed



