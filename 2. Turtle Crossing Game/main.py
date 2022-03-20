import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
carmanager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_loop = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_loop += 1
    if game_loop % 6 == 0:
        carmanager.create_cars()
    carmanager.move()

    #Detect collision with turtle
    for car in carmanager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Beam turtle back to start after crossing safely and level up
    if player.ycor() > 260:
        player.go_to_start()
        scoreboard.increase_level()
        carmanager.increase_speed()

screen.exitonclick()