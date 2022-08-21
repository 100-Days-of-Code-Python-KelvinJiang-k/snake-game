from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.high_score = self.access_data()
        self.display()
        self.color("white")
        self.goto(x=0, y=270)
        self.hideturtle()

    def display(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.display()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_data()
        self.score = 0
        self.display()

    def access_data(self):
        with open('data.txt', 'r') as file:
            data = int(file.read())
        return data

    def update_data(self):
        with open('data.txt', 'w') as file:
            file.write(str(self.high_score))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write(arg=f"GAME OVER\n    Score: {self.score}", align=ALIGNMENT, font=('Arial', 36, 'normal'))
