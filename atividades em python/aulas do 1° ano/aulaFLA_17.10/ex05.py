import turtle

le = turtle.Turtle()
le.color('red')


le.shape("turtle")
le.color('blue')  
for _ in [1, 2, 3]:
    le.forward(200)  
    le.right(120)


le.shape("classic")
le.color('green')  
for _ in [1, 2, 3, 4]:
    le.forward(200)  
    le.right(90)


