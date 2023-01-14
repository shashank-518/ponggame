from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self,):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.score}",align="center",font=('Arial',24,'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def gameover(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER", align="center",font=("Arial",24,"bold"))
        self.goto(0,-40)
        self.write(f"Your Score : {self.score}",align="center",font=('Arial',24,"bold"))