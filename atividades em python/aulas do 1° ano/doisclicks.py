import turtle

# Função para clique com o botão esquerdo
def clique_esquerdo(x, y):
    turtle.color("blue")
    turtle.circle(50)

# Função para clique com o botão direito
def clique_direito(x, y):
    turtle.color("red")
    turtle.circle(50)

# Configuração da tela
turtle.Screen().onclick(clique_esquerdo, 1)  # Botão esquerdo do mouse
turtle.Screen().onclick(clique_direito, 3)   # Botão direito do mouse

turtle.done()
