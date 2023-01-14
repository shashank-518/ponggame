from turtle import Turtle,Screen
from players import Player
from balll import Ball 
from scoreboard import Scoreboard 
# from heart import Heart
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("Black")

player = Player(-280)
player1 = Player(280)

ball = Ball() 

scoreboard = Scoreboard()

# heart = Heart()

screen.listen()
screen.onkey(player1.move_upward ,"Up")
screen.onkey(player1.move_backward ,"Down")

is_game_on = True

hearts = 2


while is_game_on:

    m=ball.moving_ball()
    player.computer_goto(m)
    ball.bounce_back()
    ball.go_back()

    if player1.head.distance(ball) < 35.0:
        scoreboard.increase()
        ball.bounce_back()
        
    else:
        if hearts > 0:
            ball.restart()
            player.restart(-280)
            player1.restart(280)
            time.sleep(0.1)
            hearts-=1
        else:
            scoreboard.gameover()
            is_game_on = False
          

        

        
screen.exitonclick()