from turtle import Turtle
import random

COLOR1 = "#%02x%02x%02x" % (255, 71, 26)  # Red
COLOR2 = "#%02x%02x%02x" % (26, 163, 255)  # Blue
COLOR3 = "#%02x%02x%02x" % (113, 218, 113)  # Green
COLOR4 = "#%02x%02x%02x" % (255, 117, 26)  # Orange
COLOR5 = "#%02x%02x%02x" % (255, 77, 196)  # Pink
COLOR6 = "#%02x%02x%02x" % (170, 128, 255)  # Software Purple
COLOR7 = "#%02x%02x%02x" % (255, 209, 26)  # Yellow
COLOR8 = "#%02x%02x%02x" % (0, 204, 204)  # Blue Green
COLOR9 = "#%02x%02x%02x" % (255, 51, 133)  # Red Pink
COLOR10 = "#%02x%02x%02x" % (204, 153, 0)  # Brown
COLOR11 = "#%02x%02x%02x" % (117, 163, 163)  # Dark Grey
COLOR12 = "#%02x%02x%02x" % (172, 0, 230)  # Dark Purple
COLOR13 = "#%02x%02x%02x" % (89, 179, 0)  # Dark Yellow Green
COLOR14 = "#%02x%02x%02x" % (172, 230, 0)  # Soft Yellow Green
COLORS = [COLOR1, COLOR2, COLOR3, COLOR4, COLOR5, COLOR6, COLOR7, COLOR8, COLOR9, COLOR10, COLOR11, COLOR12, COLOR13,
          COLOR14]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
