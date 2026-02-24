import pygame
from pygame.locals import *

JANELA_WIDTH = 900
JANELA_HEIGHT = 900
BLOCK = 20
POS_INICIAL_X = JANELA_WIDTH // 2 - BLOCK // 2
POS_INICIAL_Y = JANELA_HEIGHT // 2 - BLOCK // 2

pygame.init()

janela = pygame.display.set_mode((JANELA_WIDTH, JANELA_HEIGHT))

cobra_surface = pygame.Surface((BLOCK, BLOCK))
cobra_pos = [(POS_INICIAL_X, POS_INICIAL_Y)]
cobra_surface.fill((68,189,50))

while True:
    pygame.time.Clock().tick(10)
    janela.fill((255,255,204))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()
        
    for pos in cobra_pos:
        janela.blit(cobra_surface,pos)

    cobra_pos[0] = cobra_pos[0][0] + BLOCK, cobra_pos[0][1]
    #cobra_pos[0] = cobra_pos[0][0] - BLOCK, cobra_pos[0][1]
    cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] - BLOCK
    #cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] + BLOCK

    pygame.display.update()