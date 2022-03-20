from turtle import Turtle

COURT_WIDTH = 800
COURT_HEIGHT = 600
LEFT_EDGE = int(-(COURT_WIDTH/2))
RIGHT_EDGE = int(COURT_WIDTH/2)
TOP_EDGE = int(COURT_HEIGHT/2)
BOTTOM_EDGE = int(-COURT_HEIGHT/2)
LINE_LENGTH = 10
GAP_LENGTH = 10
INTERVAL = int(COURT_HEIGHT/(LINE_LENGTH + GAP_LENGTH))

class Court(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.pencolor("white")
        self.penup()
        self.goto(0, TOP_EDGE)
        self.seth(270)
        for length in range(INTERVAL):
            self.pendown()
            self.forward(LINE_LENGTH)
            self.penup()
            self.forward(GAP_LENGTH)