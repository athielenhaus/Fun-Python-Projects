from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_list = []

    def create_cars(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        y_start = random.randint(-250, 250)
        new_car.seth(180)
        new_car.goto(300, y_start)
        self.car_list.append(new_car)


    def move(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += 10