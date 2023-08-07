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
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

            

    
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
        
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    
    def add_score(self):
        self.score += 1
        self.update_score()


       