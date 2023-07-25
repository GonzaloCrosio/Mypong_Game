from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Create and format to screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
#Turn off the animation (and prevent previous movements from being visible)
screen.tracer(0)

# Paddle ubication
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# Ball create
ball= Ball()
# Score create
scoreboard = Scoreboard()


# Listen events
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# To activate the screen again
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # To change the speed of the ball with screen updates
    screen.update()
    ball.move()

    # Detect ball-wall collision
    if ball.ycor()>280 or ball.ycor()<-280:
        # Necesito que rebote
        ball.bounce_y()

    # Detect paddle collision. Detect if it went past the screen (320) or if it collided with the paddle (50)
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    # Detect when the right paddle loses. If the ball crosses 390, it is detected
    if ball.xcor()>390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when the left paddle loses. If the ball crosses -390, it is detected
    if ball.xcor()<-390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()