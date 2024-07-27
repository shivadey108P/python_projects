from turtle import Screen
import time
from snake import Snake
# from message_box import Pop_up
from food import Food
from scoreboard import Scoreboard

screen = Screen()
# pop = Pop_up()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snaky Sneaky')
# pop.open_pop_up('Welcome to snake game', 'Use arrow keys to move the snake')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

game_on =  True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
        
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_game()
        snake.reset_snake()
        
        
    # Detect collision with tail
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_on = False
    #         score.game_over()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_game()
            snake.reset_snake()        
        
        
screen.exitonclick()