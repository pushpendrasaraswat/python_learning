from turtle import Turtle, Screen, colormode
import random

color_list = [ (22, 149, 185), (234, 118, 46), (11, 59, 84), (228, 235, 239), (207, 66, 26)]


turtle_drawing = Turtle()
colormode(255)
turtle_drawing.shape('turtle')
turtle_drawing.speed(10)



y = -100
for _ in range(10):
    turtle_drawing.penup()
    turtle_drawing.setx(-350)
    turtle_drawing.sety(y)
    turtle_drawing.penup()
    for _ in range(10):
        turtle_drawing.dot(20, random.choice(color_list))
        turtle_drawing.penup()
        turtle_drawing.forward(80)
    y+=40






screen = Screen()
screen.exitonclick()