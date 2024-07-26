from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from pop_up_menu import Pop_up
import time

screen = Screen()
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

score = Scoreboard()

pop_message = Pop_up()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

max_score = pop_message.open_pop_up('Welcome to Pong Game', 'Choose the max score to play the game')

screen.listen()

screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')

screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    # Detect collision with top and bottom walls and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_stance()
        score.l_point()
        
    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_stance()
        score.r_point()

    # Detect if paddle goes out of screen and stop it from moving further
    if r_paddle.ycor() > 250:
        r_paddle.sety(250)  # Corrected to set paddle's position instead of changing keypress
    elif r_paddle.ycor() < -250:
        r_paddle.sety(-250)  # Corrected to set paddle's position instead of changing keypress

    if l_paddle.ycor() > 250:
        l_paddle.sety(250)  # Corrected to set paddle's position instead of changing keypress
    elif l_paddle.ycor() < -250:
        l_paddle.sety(-250)  # Corrected to set paddle's position instead of changing keypress

    # Check if the game should end
    if score.l_score == max_score or score.r_score == max_score:
        game_is_on = False
        pop_message.notify_pop_up('Game Over', f'The winner is {"Left" if score.l_score == max_score else "Right"} player with a score of {max_score}')
        screen.bye()
    
        
screen.exitonclick()
