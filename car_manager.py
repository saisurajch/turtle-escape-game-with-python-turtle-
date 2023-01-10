from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        frequency = random.randint(1,5)
        if frequency == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_len=2)
            car.penup()
            car.setheading(180)
            car.color(random.choice(COLORS))
            y_axis = random.randint(-250, 250)
            car.goto(300, y_axis)
            self.all_cars.append(car)


    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
