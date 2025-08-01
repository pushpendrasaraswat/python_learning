import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Indian States and Union Territories Games")

image = "blank_image.gif"
#screen.setup(width=800, height=900)
screen.bgpic(image)
#turtle.shape(image)

"""
def get_mouse_click(x,y):
    print(x,y)


turtle.onscreenclick(get_mouse_click)

turtle.mainloop()

this will give the coordinates of the mouse click on the screen
which will help in creating the data
"""


data = pd.read_csv("indian_state.csv")
states = len(data["State"])
turtle.hideturtle()
for i in range(states):
    answer_state = screen.textinput("Guess the state", "What's another state's name?").title()
    state_names = data[data["State"] == answer_state.title()]
    if not state_names.empty:
        turtle.penup()

        turtle.goto(x = state_names["X"].values[0], y = int(state_names["Y"].values[0]))
        turtle.pendown()
        turtle.write(state_names.State.item(), align="center", font=("Arial", 10, "normal"))

    i += 1



turtle.mainloop()
