from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1   # Ball speed. 

# Inicial ball move
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

# To change direction when it collides with the wall Y
    def bounce_y(self):
        self.y_move *= -1

# To change direction when it collides with the wall X
    def bounce_x(self):
        self.x_move *=-1
        self.move_speed *= 0.8    # More speed for ball

# To return to the starting position when there is a 'goal' and change direction
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1  # Original speed to restart
        self.bounce_x()