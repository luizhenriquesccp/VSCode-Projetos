from turtle import Turtle, onscreenclick, onkey, listen, Screen
le = Turtle()
tela = Screen()

le.left(90)
le.goto(0, -500)
le.goto(0, 500)
le.goto(0, 0)
le.right(90)
le.goto(-500, 0)
le.goto(500, 0)
le.goto(0, 0)

def goto_and_mark(x, y):
    le.pendown()
    le.goto(x, y)
    
le.penup()
le.goto(goto_and_mark)


for _ in range(4):
    le.forward(100)
    le.right(90)

le.penup()
le.goto(onscreenclick)

le.circle(70)

le.penup()
le.goto(onscreenclick)

le.forward(-100)
for _ in range(2):
    le.forward(200)
    le.right(90)
    le.forward(60)
    le.right(90)




listen()
tela.mainloop()
