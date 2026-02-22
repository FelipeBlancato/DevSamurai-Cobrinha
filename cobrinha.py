import pygame
from pygame.locals import *

JANELA_WIDTH = 600
JANELA_HEIGHT = 600
BLOCK = 20
POS_INICIAL_X = 290
POS_INICIAL_Y = 290

pygame.init()

janela = pygame.display.set_mode((JANELA_WIDTH, JANELA_HEIGHT))
janela.fill((255,255,204))

cobra_surface = pygame.Surface((BLOCK, BLOCK))
cobra_pos = [(POS_INICIAL_X, POS_INICIAL_Y)]
cobra_surface.fill((68,189,50))

while True:

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()
    
    for pos in cobra_pos:
        janela.blit(cobra_surface,pos)

    pygame.display.update()