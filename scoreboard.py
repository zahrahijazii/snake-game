from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto((0,270))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()


       