import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, GameOver

# screen props
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Turtle Escape")
screen.tracer(0)

# initialisation
player = Player()
cars = CarManager()
score = Scoreboard(x=-210,y=260)
game_over = GameOver()
# keypress
screen.listen()
screen.onkey(player.move,"w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    # Detecting Collisions with cars
    for i in cars.all_cars:
        if player.distance(i) < 20:
            game_over.true()
            game_is_on = False

    # Detect finish point
    if player.ycor() > 280:
        player.is_at_finish_line()
        score.add_score()
        cars.increase_speed()

screen.exitonclick()
