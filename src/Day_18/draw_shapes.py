from random import choice
from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.speed(10)

shapes = [{"shape": "triangle", "side": 3}, {"shape": "square", "side": 4}, {"shape": "pentagon", "side": 5},
          {"shape": "heptagon", "side": 6}, {"shape": "octagon", "side": 8}, {"shape": "nonagon", "side": 9},
          {"shape": "decagon", "side": 10}]

colors = ["cornflowerBlue", "DarkOrchid", "IndianRed", "LightSeaGreen", "wheat", "SeaGreen"]


def draw_shapes(shape, color):
    angle = 360 / shape["side"]
    for _ in range(shape["side"]):
        turtle.color(color)
        turtle.forward(100)
        turtle.left(angle)


for shape in shapes:
    color_choice = random.choice(colors)
    draw_shapes(shape, color_choice)

screen_draw = Screen()
screen_draw.exitonclick()
