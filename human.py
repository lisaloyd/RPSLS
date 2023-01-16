from player import Player


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def display_choices(self):
        print()
        for count in range(len(self.gesture_list)):
            gesture = self.gesture_list[count]
            print(count + 1, gesture)

    def choose_gesture(self):
        self.display_choices()

        index = int(input("Choose a number from the above list ")) - 1
        self.gesture = self.gesture_list[index]
        print()
        print(f'{self.name} chooses {self.gesture}')

       # if self.choose == '1':
        #    print()
         #   print(f"Player has chosen {self.gesture_list[0]}!")
    #    elif self.choose == '2':
     #       print()
      #      print(f"Player has chosen {self.gesture_list[1]}!")
    #    elif self.choose == '3':
     #       print()
      #      print(f"Player has chosen {self.gesture_list[2]}!")
      #  elif self.choose == '4':
       #     print()
        #    print(f"Player has chosen {self.gesture_list[3]}!")
      #  elif self.choose == '5':
       #     print()
        #    print(f"Player has chosen {self.gesture_list[4]}")
      #  else:
       #     while self.choose != '1' or '2' or '3' or '4,' or '5':
        #        print("That is not an option. ")
         #       break

   

