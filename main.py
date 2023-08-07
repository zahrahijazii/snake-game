from turtle import Screen
import time 
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    #Detect collision with snake and food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.add_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset()

    #Detect collision with tail  
    for segament in snake.segaments[1:]:
        if snake.head.distance(segament) < 10:
            score.reset_score()
            snake.reset()
    
     



    snake.move()

























screen.exitonclick()