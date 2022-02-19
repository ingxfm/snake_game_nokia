from turtle import Turtle, Screen


POSITION = (-30, 230)
POSITION_FINAL = (-45, 0)
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("red")
        self.goto(POSITION)
        self.ht()
        self.show_it()

    def show_it(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT)

    def finish_message(self):
        self.goto(POSITION_FINAL)
        self.clear()
        self.write(f"GAME OVER. Your score is: {self.score}.", align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
