# number of turtles
# different colors
# direction
# speed
# stop at the end of the screen

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
race_on = False
user_guess = screen.textinput(title='Make a guess', prompt="Which turtle will win the race ? Enter a color:")
print(user_guess)
y_direction = [-70, -40, -10, 20, 50, 80]
colours = ['Red', 'Green', 'Blue', 'wheat', 'orange', 'yellow']
all_turtles = []

for turtle_index in range(0, 6):
    rogers = Turtle()
    rogers.shape('turtle')
    rogers.penup()
    rogers.color(colours[turtle_index])
    rogers.goto(x=-230, y=y_direction[turtle_index])
    all_turtles.append(rogers)

if user_guess:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if user_guess == winning_color:
                print('You won!')
            else:
                print('you lost')
        else:
            random_distance = random.randint(0,10)
            turtle.forward(random_distance)

screen.exitonclick()