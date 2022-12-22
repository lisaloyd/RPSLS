from player import Player


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def display_choices(self):
        # for gesture in self.gesture_list:
        #     print(gesture)
        for count in range(len(self.gesture_list)):
            gesture = self.gesture_list[count]
            print(count + 1, gesture)
            # print(count + 1)

   
    def choose_gesture(self):
        #
        #display gestures to user
        #ask user for gesture from list above, store input into variable
        #compare from list
        #or
        #use user input to index gesture list
        pass

