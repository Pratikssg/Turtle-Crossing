from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.increase_level()
        self.hideturtle()

    def increase_level(self):
        self.clear()
        self.goto(-290, 260)
        self.write(f"level: {self.level}", align="left", font=FONT)
        self.level += 1

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
