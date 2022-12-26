from player import Player


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def display_choices(self):
        # for gesture in self.gesture_list:
        #     print(gesture)
        print()
        for count in range(len(self.gesture_list)):
            gesture = self.gesture_list[count]
            print(count + 1, gesture)
            # print(count + 1)

   
    def choose_gesture(self):
        print()
        self.choose = input("Choose a number from above list ")
        print()
        if self.choose == [1, 2, 3, 4, 5]:
            print()
            print(f"Player has chosen {self.choose}!")
        else:
            print("That is not an option")


    
        #ask user for gesture from list above, store input into variable
        #compare from list
        #or
        #use user input to index in gesture list
