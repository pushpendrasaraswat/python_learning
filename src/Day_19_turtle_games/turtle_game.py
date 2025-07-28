from turtle import Turtle
import random

class TurtleGame:


    def __init__(self):
        self.colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
        self.turtles = []
        self.winner_color = ""


    def create_turtle(self,color, y):
        turtle = Turtle("turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(-230, y)
        self.turtles.append(turtle)

    def check_winner(self,turtle):
        x_position = int(turtle.xcor())
        if x_position <= 180:
            return False
        else:
            self.winner_color = turtle.pencolor()
            return True

    def play_game(self):
        y = -120
        for color in self.colors:
            self.create_turtle(color, y)
            y += 40
        turtle = random.choice(self.turtles)
        while not self.check_winner(turtle):
            turtle = random.choice(self.turtles)
            turtle.penup()
            turtle.forward(20)