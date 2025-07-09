import turtle


tela = turtle.Screen()


tartaruga = turtle.Turtle()
tartaruga.speed(1)  


def desenhar_quadrado(x, y):
    tartaruga.penup()  
    tartaruga.goto(x, y)  
    tartaruga.pendown()  

    for _ in range(4):
        tartaruga.forward(100)  
        tartaruga.right(90)  


tela.onclick(desenhar_quadrado)


turtle.done()
