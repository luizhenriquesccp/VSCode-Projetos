from turtle import Turtle, onscreenclick

le = Turtle()
desenho_atual = None
raio_circulo = 45
quadrados_ocupados = []

le.pensize(5)
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

def goto_and_mark(x, y):
    le.penup()
    le.goto(x - (x % 100) + 50, y - (y % 100) + 50)
    le.pendown()

def circulo(x, y):
    if -100 < x < 200 and -100 < y < 200:
        le.pensize(10)
        le.pencolor("blue")
        if not check_overlap(x, y, raio_circulo * 2):
            goto_and_mark(x, y)
            le.penup()
            le.left(90)
            le.forward(-45)
            le.right(90)
            le.pendown()
            le.circle(raio_circulo)
            quadrados_ocupados.append((x, y))

def desenha_x(x, y):
    if -100 < x < 200 and -100 < y < 200:
        le.pensize(20)
        if not check_overlap(x, y, raio_circulo * 2):
            goto_and_mark(x, y)
            le.pencolor('red')
            le.right(45)
            le.forward(45)
            le.backward(90)
            le.forward(45)
            le.left(90)
            le.forward(46)
            le.backward(90)
            le.right(45)
            quadrados_ocupados.append((x, y))

def check_overlap(x, y, distance):
    for pos_x, pos_y in quadrados_ocupados:
        if ((x - pos_x) ** 2 + (y - pos_y) ** 2) ** 0.5 < distance:
            return True
    return False

def on_mouse_click(x, y):
    global desenho_atual
    
    if desenho_atual is None or desenho_atual == desenha_x:
        desenho_atual = circulo
    else:
        desenho_atual = desenha_x
        
    desenho_atual(x, y)

onscreenclick(on_mouse_click)

le.screen.mainloop()
