class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]  
        self.gesture = ''

    def choose_gesture(self):
        pass

    def score_point(self):
        self.score += 1
        print(f'{self.name} wins the round!')
