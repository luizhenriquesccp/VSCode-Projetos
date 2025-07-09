import turtle

turtle = turtle.Turtle()
turtle.shape("turtle")  
turtle.pensize(3)  

for color in ['pink', 'red', 'black', 'blue']:  
    turtle.color(color)

for _ in range(2):  
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.penup()  
    turtle.forward(120)  
    turtle.pendown()  


