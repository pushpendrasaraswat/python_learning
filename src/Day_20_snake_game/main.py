from turtle import Turtle, Screen
import time
from snake import Snake
# This is the main file for the Snake Game project
# create turtle and screen objects

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



screen.update()
game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.5)











screen.exitonclick()












