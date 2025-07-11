import pygame
import sys

def desenha_circulo(posicao):
    pygame.draw.circle(screen, (255, 0, 0), posicao, 30)
    pygame.display.flip()

pygame.init()

largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desenhar Círculo")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            desenha_circulo(evento.pos)

pygame.quit()
sys.exit()
