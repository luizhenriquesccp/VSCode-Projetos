import turtle
import random

le = turtle.Turtle()
colors = ['purple', 'blue', 'green', 'orange', 'red']  

le.left(30)  

colors.remove('red')  

le.pensize(2)  

for _ in [1, 2, 3]:
    color = random.choice(colors)
    le.color(color)
    le.forward(100)
    le.right(120)
