import turtle
le =turtle.Turtle()
tela = turtle.Screen()

le.penup()
le.goto(0, 100)
le.pendown()
le.forward(-100)
le.forward(300)
le.penup()
le.goto(0, 0)
le.pendown()
le.forward(-100)
le.forward(300)
le.penup()
le.goto(0, 100)
le.pendown()
le.left(90)
le.forward(100)
le.forward(-300)
le.penup()
le.goto(100, 100)
le.pendown()
le.forward(100)
le.forward(-300)
le.setheading(0)


def clique_esquerdo(x, y):
    le.color("blue")
    le.left(90)
    le.penup()
    le.forward(-45)
    le.pendown()
    le.right(90)
    le.circle(45)
    



def clique_direito(x, y):
    le.color("red")
    le.left(40)
    le.forward(-45)
    le.forward(90)
    le.forward(-45)
    le.left(90)
    le.forward(-45)
    le.forward(90)
    le.forward(-45)
    le.right(130)
    le.setheading(0)

def um():
    le.penup()
    le.goto(-50, 150)
    le.pendown()

def dois():
    le.penup()
    le.goto(50, 150)
    le.pendown()

def treis():
    le.penup()
    le.goto(150, 150)
    le.pendown()

def quatro():
    le.penup()
    le.goto(-50, 50)
    le.pendown()

def cinco():
    le.penup()
    le.goto(50, 50)
    le.pendown()

def seis():
    le.penup()
    le.goto(150, 50)
    le.pendown()

def sete():
    le.penup()
    le.goto(-50, -50)
    le.pendown()

def oito():
    le.penup()
    le.goto(50, -50)
    le.pendown()

def nove():
    le.penup()
    le.goto(150, -50)
    le.pendown()


    

turtle.listen()
turtle.onkey(um, "1")
turtle.onkey(dois, "2")
turtle.onkey(treis, "3")
turtle.onkey(quatro, "4")
turtle.onkey(cinco, "5")
turtle.onkey(seis, "6")
turtle.onkey(sete, "7")
turtle.onkey(oito, "8")
turtle.onkey(nove, "9")


turtle.Screen().onclick(clique_esquerdo, 1)  
turtle.Screen().onclick(clique_direito, 3)   


turtle.done()