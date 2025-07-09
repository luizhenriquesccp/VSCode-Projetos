import turtle
import random

le = turtle.Turtle()

colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'orange', 'red', "black"] 
le.pensize(3)  

for _ in range(15):  
    color = random.choice(colors)
    le.color(color)
    le.forward(100)
    le.backward(100)
    le.right(25)

