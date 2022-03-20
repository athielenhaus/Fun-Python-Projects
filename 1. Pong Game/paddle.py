from turtle import Turtle
from court import LEFT_EDGE, TOP_EDGE, BOTTOM_EDGE,RIGHT_EDGE

UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.color("white")
        self.goto(position)

    def up(self):
        if self.ycor() < TOP_EDGE - 50:
            new_ycor = self.ycor() + 20
            self.sety(new_ycor)


    def down(self):
        if self.ycor() > BOTTOM_EDGE + 50:
            new_ycor = self.ycor() - 20
            self.sety(new_ycor)


