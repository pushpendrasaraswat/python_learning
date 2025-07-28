from turtle import Turtle, Screen



turtle = Turtle()
turtle.speed(10)

y=0
for _ in range(10):
    turtle.setx(0)
    turtle.sety(y)
    y+=10
    for _ in range(10):
        turtle.dot(5)
        turtle.penup()
        turtle.forward(10)





screen_turtle = Screen()

screen_turtle.exitonclick()