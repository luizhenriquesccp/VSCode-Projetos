import turtle

le = turtle.Turtle()

le.pencolor("blue")
le.pensize(2)

for _ in range(5):
	le.forward(100)
	le.right(36)
	le.forward(100)
	le.left(108)


turtle.exitonclick()
