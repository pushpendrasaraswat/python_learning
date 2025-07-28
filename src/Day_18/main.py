from turtle import Turtle, Screen


turtle = Turtle()
turtle.shape("turtle")
turtle.color("blue")

turtle.speed(1)

for _  in range(4):
    turtle.forward(100)
    turtle.left(90)






screen = Screen()
screen.setup(800, 600)
screen.exitonclick()


