from turtle import Turtle
from court import  TOP_EDGE
ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_player1 = 0
        self.score_player2 = 0
        self.penup()
        self.goto(0, TOP_EDGE - 50)
        self.speed("fastest")
        self.pencolor("white")
        self.hideturtle()
        self.write(f"{self.score_player1} {self.score_player2}", False, align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.clear()
        self.write(f"{self.score_player1} {self.score_player2}", False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)