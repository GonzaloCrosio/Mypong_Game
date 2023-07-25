from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  # Hide Turtle
        self.l_score = 0   # Score left player
        self.r_score = 0   # Score right player
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)                                                       # Score location left player
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))   # Fomart score left player
        self.goto(100, 200)                                                        # Score location right player
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))   # Fomart score right player

    # Score +1 left player
    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()

    # Score +1 right player
    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()

