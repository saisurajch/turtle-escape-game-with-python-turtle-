from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x,y)
        self.add_score()

    def add_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)
        self.score += 1

class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()

    def true(self):
        self.clear()
        self.write(f"Game Over!", align="center", font=FONT)
