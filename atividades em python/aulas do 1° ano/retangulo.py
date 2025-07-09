import turtle

le = turtle.Turtle()

le.pencolor("blue")
le.pensize(2)


le.left(90)
for _ in range(2):
	le.forward(200)
	le.right(90)
	le.forward(100)
	le.right(90)
