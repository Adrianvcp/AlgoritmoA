# -*- coding: utf-8 -*-
import time
import os
import random
import threading
import pygame


NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

def cargarTexturas():

        texturas = []
        fondo = "texturas/fondocancha.png"
        muro = "texturas/jugador2.png"
        entrada = "texturas/jugador.png"
        salida = "texturas/jugador.png"
        personaje = "texturas/jugador.png"

        
        s0 = pygame.image.load(fondo)
        #s0 = pygame.Surface(dimTextura)
        texturas.append(s0)

        s1 = pygame.image.load("texturas/jugador2.png")
        #s1 = pygame.Surface(dimTextura)

        texturas.append(s1)
        s2 = pygame.image.load(entrada)
        #s2 = pygame.Surface(dimTextura)
        texturas.append(s2)

        s3 = pygame.image.load(salida)
        #s3 = pygame.Surface(dimTextura)
        texturas.append(s3)

        s4 = pygame.image.load(personaje)
        #s4 = pygame.Surface(dimTextura)
        texturas.append(s4)

        return texturas


mapaBit = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]] 

salida = ""

fil = len(mapaBit)
col = len(mapaBit[0])

TAM_TEXTURA = 63
dimx = col * TAM_TEXTURA
dimy = fil * TAM_TEXTURA
dimTextura = [TAM_TEXTURA, TAM_TEXTURA]



pygame.init()

pygame.display.set_caption("Laberinto")
pantalla = pygame.display.set_mode([600, 600])
texturas = cargarTexturas()

while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pantalla.blit(texturas[0], [0,0])  # "T"
                
    for f in range(fil):
            for c in range(col):

                if mapaBit[f][c] == 1:
                    pantalla.blit(texturas[1], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # "#"
                if mapaBit[f][c] == 2:
                    pantalla.blit(texturas[2], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # "T"
                if mapaBit[f][c] == 3:
                    pantalla.blit(texturas[3], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # "S"
                if mapaBit[f][c] == 4:
                    pantalla.blit(texturas[0], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # "." En caso de haber

    pygame.display.update()


