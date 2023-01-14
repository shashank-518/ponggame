from turtle import Turtle
 

class Player:

    def __init__(self,user):
        self.segment =[]
        self.create_player(user)
        self.head = self.segment[0]

    def create_player(self,user):
        new = Turtle()
        new.shape("square")
        new.shapesize(1,2.8)
        new.penup()
        new.color("white")
        new.speed(10)
        new.goto(user,0)
        new.setheading(90)
        self.segment.append(new)


    def move_upward(self):
        self.head.forward(40)

    def move_backward(self):
        self.head.backward(40)

    def computer_goto(self,m):
        self.head.goto(-280,m)
    
    def restart(self,user):
        self.head.goto(user,0)
        

