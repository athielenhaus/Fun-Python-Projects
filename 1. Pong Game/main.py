import turtle
from court import Court, COURT_HEIGHT, COURT_WIDTH, LEFT_EDGE, TOP_EDGE, BOTTOM_EDGE
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=COURT_WIDTH, height=COURT_HEIGHT)
screen.tracer(0)


court = Court()
paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

sleep_time = 0.1
game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    if ball.ycor() >= TOP_EDGE - 20 or ball.ycor() <= BOTTOM_EDGE + 20:
        ball.bounce()

    # Detect collision with right paddle
    if ball.xcor() >= 330 and ball.distance(paddle_right) < 60:
        ball.hit()
        sleep_time *= 0.9

    # Detect collision with left paddle
    if ball.xcor() <= -330 and ball.distance(paddle_left) < 60:
        ball.hit()
        sleep_time *= 0.9

    # Detect miss
    if ball.xcor() < -360:
        scoreboard.score_player2 += 1
        scoreboard.update_score()
        ball.reset_position()
        sleep_time = 0.1

    if ball.xcor() > 360:
        scoreboard.score_player1 += 1
        scoreboard.update_score()
        ball.reset_position()
        sleep_time = 0.1


    turtle.listen()
    screen.onkey(paddle_right.up, "Up")
    screen.onkey(paddle_right.down, "Down")
    screen.onkey(paddle_left.up, "w")
    screen.onkey(paddle_left.down, "s")






screen.exitonclick()