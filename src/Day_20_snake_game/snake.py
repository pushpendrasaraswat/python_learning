from turtle import Turtle
import random

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.nodes = []
        self.create_snake()
        self.head = self.nodes[0]
        self.new_node = None
        self.counter = 0


    def create_snake(self):
        for position in STARTING_POSITION:
            new_node = Turtle("square")
            new_node.color("white")
            new_node.penup()
            new_node.goto(position)
            self.nodes.append(new_node)

    def move(self):
        self.consume_fruit()
        self.generate_fruit()
        for turtle_number in range(len(self.nodes) - 1, 0, -1):
            new_x = self.nodes[turtle_number - 1].xcor()
            new_y = self.nodes[turtle_number - 1].ycor()
            self.nodes[turtle_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        print(self.head.heading())
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  # 90 degrees is up
        self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        self.move()

    def generate_random_fruit(self):
        node = Turtle("circle") # Create a new turtle for the fruit
        node.color("red")
        node.penup()
        x = random.choice(range(-280, 281, 20))
        y = random.choice(range(-280, 281, 20))
        node.goto(x, y)
        self.new_node = node


    def generate_fruit(self):
        if int(self.counter % 10) == 0 and self.new_node is None:
            self.generate_random_fruit()
        else:
            self.counter += 5


    def consume_fruit(self):
        if self.new_node is not None:
            if int(self.head.xcor()) == int(self.new_node.xcor()) and int(self.head.ycor()) == int(self.new_node.ycor()):
                self.new_node.color("white")
                self.new_node.shape("square")
                self.nodes.append(self.new_node)
                self.new_node = None