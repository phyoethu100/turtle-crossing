from turtle import Turtle

FONT = ("Arial", 22, "normal")
GAME_OVER = ("Arial", 44, "normal")
COLOR1 = "#%02x%02x%02x" % (0, 97, 77)
COLOR2 = "#%02x%02x%02x" % (0, 128, 128)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_level()
        self.goto(280, 250)
        self.update_score()

    def update_level(self):
        self.clear()
        self.goto(-280, 250)
        self.color(COLOR1)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_score(self):
        self.goto(280, 250)
        self.color(COLOR1)
        self.write(f"Score: {self.score}", align="right", font=FONT)

    def increase_score(self):
        self.score += 10
        self.update_score()

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.color(COLOR2)
        self.write("GAME OVER", align="center", font=GAME_OVER)