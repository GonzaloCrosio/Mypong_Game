from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")        # To create a square shape for the paddle
        self.color("white")         # To paddle colors
        self.shapesize(stretch_len=1, stretch_wid=5)    # As the turtle measures 20x20 in its original form, multiply the width by 5 to make it wider
        self.penup()                # Hide paddle
        self.goto(position)         # Paddle position 

    # Function to up paddle
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Function to down paddle
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



