from turtle import Turtle, Screen
from turtle_game import TurtleGame


screen = Screen()
screen.setup(500, 400)

turtleGame = TurtleGame()

user_color = screen.textinput("Turtle Racing", "which turtle will win the race enter the color :")

turtleGame.play_game()



if turtleGame.winner_color.lower() == user_color.lower():
    print(f"you won , your color was :  {user_color} and winner color was : {turtleGame.winner_color}")
else :
    print(f"you loose , your color was :  {user_color} and winner color was : {turtleGame.winner_color}")

screen.exitonclick()
