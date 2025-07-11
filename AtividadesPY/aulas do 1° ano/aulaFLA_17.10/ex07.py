import turtle

turtle = turtle.Turtle()
turtle.color('green')

for _ in range(4):
    turtle.left(90)
    turtle.backward(80)


turtle.backward(170)
turtle.right(90)

for _ in range(3):
  turtle.forward(80)
  turtle.left(90)