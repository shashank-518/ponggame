from turtle import Turtle
import random

X_POSITION = -280
A_LIST = [-300,300]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")

    def moving_ball(self):
        y_position = random.randint(-300,300)
        self.speed(1)
        self.goto(X_POSITION,y_position)
        return y_position

    def bounce_back(self):
        xxx = random.randint(0,100)
        self.goto(xxx,-280)

    def go_back(self):
        yy = random.randint(-280,280)
        self.goto(280,yy)

    def restart(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()






