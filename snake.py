from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0 ), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segaments = []
        self.create_snake()
        self.head = self.segaments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segament = Turtle("square")
            new_segament.color("white")
            new_segament.penup()
            new_segament.goto(position)
            self.segaments.append(new_segament)

    def move(self):
        for seg_num in range(len(self.segaments) - 1, 0 , -1): 
            new_x = self.segaments[seg_num - 1].xcor() 
            new_y = self.segaments[seg_num - 1].ycor()
            self.segaments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)
    
    def right(self):
        self.head.setheading(0)




        

