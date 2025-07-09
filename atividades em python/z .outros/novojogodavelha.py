from turtle import Turtle, onscreenclick

le = Turtle()
desenho_atual = None 

le.penup()
le.goto(-150, 150)  
le.pendown()
le.forward(300)
le.penup()
le.goto(-150, 50)
le.pendown()
le.forward(300)
le.penup()
le.goto(-50, 150)  
le.pendown()
le.left(90)
le.forward(100)
le.forward(-300)
le.penup()
le.goto(50, 150)  
le.pendown()
le.forward(100)
le.forward(-300)
le.setheading(0)

def goto_and_mark(x, y):
    le.penup()
    le.goto(x - (x % 100) + 50, y - (y % 100) + 50)
    le.pendown()


raio = 40

def circulo(x, y):
    if -100 < x < 200 and 0 < y < 300:
        le.pensize(10)
        le.pencolor("blue")
        goto_and_mark(x, y)
        le.penup()
        y_atual = le.ycor()
        novo_y = y_atual - raio
        le.sety(novo_y)
        le.pendown()
        le.circle(40)

def desenha_x(x, y):
    if -100 < x < 200 and 0 < y < 300:
        le.pensize(20)
        goto_and_mark(x, y)
        le.pencolor('red')
        le.right(45)
        le.forward(40)
        le.backward(80)
        le.forward(40)
        le.left(90)
        le.forward(40)
        le.backward(80)
        le.right(45)

def on_mouse_click(x, y):
    global desenho_atual
    
    if desenho_atual is None or desenho_atual == desenha_x:
        desenho_atual = circulo
    else:
        desenho_atual = desenha_x
        
    desenho_atual(x, y)

onscreenclick(on_mouse_click)

le.screen.mainloop()
