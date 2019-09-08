import pygame
import os
import time



class nodo():
    def __init__(self,padre=None,pos=None):
        self.padre = padre
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __eq__(self, other):
        return self.pos == other.pos

def a_algorit(matriz,pos_ini,pos_final,pantalla):
    #Listas
    L_Abiertas = []
    L_Cerradas = []
    #Nodo inicio y fin
    N_inicio = nodo(None,pos_ini)
    N_Fin = nodo(None,pos_final)

    L_Abiertas.append(N_inicio)
    texturas2 = cargarImagenes()

    while len(L_Abiertas) > 0:
        
        ndoActual = L_Abiertas[0]
        ndoActual_i = 0
        
        for index, item in enumerate(L_Abiertas):
            if item.f < ndoActual.f:
                ndoActual = item
                ndoActual_i = index

        L_Abiertas.pop(ndoActual_i)
        L_Cerradas.append(ndoActual)

    
        if ndoActual == N_Fin:
            path = []
            current = ndoActual
            while current is not None:
                path.append(current.pos)
                current = current.padre
            return path
        
        ndosVecinos = []
        for variacion in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: 
            node_position = (ndoActual.pos[0] + variacion[0], ndoActual.pos[1] + variacion[1]) #pos
            #Limite
            if node_position[0] > (len(matriz) - 1) or node_position[0] < 0 or node_position[1] > (len(matriz[len(matriz)-1]) -1) or node_position[1] < 0:
                continue
            caminarPersonaje(len(matriz),len(matriz[0]),matriz,pantalla,texturas2,63,node_position) #dib pos
            time.sleep(1)
            #Disponible ?
            if matriz[node_position[0]][node_position[1]] != 0:
                continue
            


            if variacion == (1,1) or variacion == (-1,-1) or variacion == (-1,1) or variacion == (1,-1): 
                new_node = nodo(ndoActual, node_position)
                new_node.g = 14
            else:
                new_node = nodo(ndoActual, node_position)
                new_node.g = 10
            ndosVecinos.append(new_node) 


            for dat in ndosVecinos:
                if dat in L_Cerradas:   continue
                dat.h = ((dat.pos[0] - N_Fin.pos[0]) ** 2) + ((dat.pos[1] - N_Fin.pos[1]) ** 2)
                dat.f = dat.g + dat.h
                for open_node in L_Abiertas:
                    if dat == open_node and dat.g > open_node.g:continue
                L_Abiertas.append(dat)

def cargarImagenes():
    img = []
    fondo = "img/fondocancha.png"
    muro = "img/jugador2.png"
    entrada = "img/jugador.png"
    salida = "img/jugador.png"
    error = "img/JugadorEliminado.png"

    
    img.append(pygame.image.load(fondo))
    img.append(pygame.image.load(muro))
    img.append(pygame.image.load(entrada))
    img.append(pygame.image.load(salida))
    img.append(pygame.image.load(error))
    return img

def mapaDibujo(fil,col,mapaBit,pantalla,texturas,TAM_TEXTURA):
    for f in range(fil):
            for c in range(col):
                if mapaBit[f][c] == 1:
                    pantalla.blit(texturas[1], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # "#"
                if mapaBit[f][c] == 2:
                    pantalla.blit(texturas[2], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # "T"
                if mapaBit[f][c] == 3:
                    pantalla.blit(texturas[3], [c * TAM_TEXTURA, f * TAM_TEXTURA])  # "S"


def caminarPersonaje(fil,col,mapaBit,pantalla,texturas,TAM_TEXTURA,nodo):
    #mapaDibujo(fil,col,mapaBit,pantalla,texturas,TAM_TEXTURA)
    
    pantalla.blit(texturas[2], [nodo[1] * TAM_TEXTURA, nodo[0] * TAM_TEXTURA])
    pygame.display.update()



def main():
    mapaBit = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [2, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 3],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]] 
    
    start = (2,0)
    end = (5,8)
    
    
    fil = len(mapaBit)
    col = len(mapaBit[0])
    TAM_TEXTURA = 63
    pygame.init()
    pygame.display.set_caption("Laberinto")
    pantalla = pygame.display.set_mode([600, 600])
    texturas = cargarImagenes()

    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
        pantalla.blit(texturas[0], [0,0])  #cancha
        
        
        mapaDibujo(fil,col,mapaBit,pantalla,texturas,TAM_TEXTURA) #Texturas
        path = a_algorit(mapaBit,start,end,pantalla)
        print(path)
    
        pygame.display.update()

if __name__ == '__main__':
    main()