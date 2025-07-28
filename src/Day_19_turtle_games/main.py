from  turtle import Turtle, Screen

turtle = Turtle()
turtle.color("black")

screen = Screen()

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def move_counter_clock_wise():
    turtle.left(35)

def move_clock_wise():
    turtle.right(30)

def reset_turtle():
    turtle.reset()  # This will clear the screen and reset the turtle's position

# this is how we listen to the key press or events
screen.listen()
screen.onkey(key ="w",fun=move_forward)
screen.onkey(key ="s",fun=move_backward)
screen.onkey(key ="a",fun=move_counter_clock_wise)
screen.onkey(key ="d",fun=move_clock_wise)
screen.onkey(key ="c",fun=reset_turtle)



screen.exitonclick()








