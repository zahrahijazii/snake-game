from turtle import Screen, Turtle
import time 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0 ), (-40, 0)]

segaments = []

for position in starting_position:
    new_segament = Turtle(shape="square")
    new_segament.color("white")
    new_segament.penup()
    new_segament.goto(position)
    segaments.append(new_segament)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segaments) - 1, 0 , -1): 
        new_x = segaments[seg_num - 1].xcor() 
        new_y = segaments[seg_num - 1].ycor()
        segaments[seg_num].goto(new_x, new_y)
    segaments[0].forward(20)

























screen.exitonclick()