from turtle import Turtle, onscreenclick, exitonclick

le = Turtle()
desenho_atual = None
jogo = [[' ']*3 for _ in range(3)]  

le.speed(30)
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
le.speed(8)

def goto_and_mark(x, y):
    le.penup()
    le.goto(x - (x % 100) + 50, y - (y % 100) + 50)
    le.pendown()
    
raio = 45

def circulo(x, y):
    if -100 < x < 200 and -100 < y < 200:
        le.pensize(10)
        le.pencolor("blue")
        goto_and_mark(x, y)
        le.penup()
        y_atual = le.ycor()
        novo_y = y_atual - raio
        le.sety(novo_y)
        le.pendown()
        le.circle(raio)
        marcar_jogo(x, y, 'O')
        verificar_vitoria('O')     

def desenhar_x(x, y):
    if -100 < x < 200 and -100 < y < 200:
        le.pensize(20)
        goto_and_mark(x, y)
        le.pencolor('red')
        le.right(45)
        le.forward(45)
        le.backward(90)
        le.forward(45)
        le.left(90)
        le.forward(45)
        le.backward(90)
        le.right(45)
        marcar_jogo(x, y, 'X')
        verificar_vitoria('X')

def marcar_jogo(x, y, jogador):
    linha = 2 - int(y + 100) // 100
    coluna = int(x + 100) // 100
    jogo[linha][coluna] = jogador

def desenha_linha(x1, y1, x2, y2):
    le.penup()            
    le.color("green")
    le.goto(x1, y1)        
    le.pendown()          
    le.goto(x2, y2)  

def verificar_vitoria(jogador):
    for linha, marks in enumerate(jogo):
        if all(mark == jogador for mark in marks):
            
            y = 100 - linha * 100
            desenha_linha(-100, y + 50, 200, y + 50)  
            print(f"Vitória para {jogador} na linha!")         
            exitonclick()
    
    for coluna in range(3):
        if all(jogo[linha][coluna] == jogador for linha in range(3)):
            x = coluna * 100
            desenha_linha(x - 50, 200, x - 50, -100)  
            print(f"Vitória para {jogador} na coluna!")            
            exitonclick()

    if all(jogo[i][i] == jogador for i in range(3)):
        desenha_linha(-100, 200, 200, -100)   
        print(f"Vitória para {jogador} na diagonal!")       
        exitonclick()
    elif all(jogo[i][2 - i] == jogador for i in range(3)):
        desenha_linha(-100, -100, 200, 200)   
        print(f"Vitória para {jogador} na diagonal!")        
        exitonclick()

def on_mouse_click(x, y):
    global desenho_atual

    if desenho_atual is None or desenho_atual == desenhar_x:
        desenho_atual = circulo
    else:
        desenho_atual = desenhar_x

    desenho_atual(x, y)

onscreenclick(on_mouse_click)

le.screen.mainloop()
