from turtle import Turtle, Screen

screen = Screen()
rogers = Turtle()
screen.setup(width=500,height=400)

rogers.shape('turtle')
rogers.color('red')
# rogers.forward(100)
# rogers.left(90)
# rogers.forward(100)
# rogers.left(90)
# rogers.forward(100)
# rogers.left(90)
# rogers.forward(100)
for _ in range(4):
    rogers.forward(100)
    rogers.left(90)

screen.exitonclick()

