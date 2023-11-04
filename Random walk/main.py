from turtle import Turtle, Screen
import random

screen = Screen()
rogers = Turtle()
screen.setup(width=500,height=400)
colours = ['Red', 'Green', 'Blue', 'wheat', 'orange']
direction = [0, 90, 180, 270]
rogers.pensize(5)

for _ in range(20):
    rogers.color(random.choice(colours))
    rogers.forward(35)
    rogers.left(random.choice(direction))



screen.exitonclick()