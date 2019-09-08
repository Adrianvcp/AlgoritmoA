import pygame
import os
import time

#Tamaño de la pantalla
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 920

#Tamaño de cada textura
TAM_TEXTURA = 40

#Posicion inicial de la pantalla de juego
x = 100
y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#Matriz del juego
mapaBit = [
        #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 2
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 4
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 5
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 6
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], # 7
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], # 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], # 10
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0], # 11
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], # 12
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], # 13
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], # 14
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 15
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 16
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 17
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 18
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 19
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 20
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 21
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 22
        ]

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

            #Disponible ?
            if matriz[node_position[0]][node_position[1]] == 1:
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
    background = "img/background.png"
    muro = "img/jugador2.png"
    entrada = "img/jugador.png"
    salida = "img/jugador.png"
    error = "img/JugadorEliminado.png"
    main_screen_background = "img/main_screen.png"

    
    img.append(pygame.image.load(fondo))                  # 0
    img.append(pygame.image.load(muro))                   # 1
    img.append(pygame.image.load(entrada))                # 2
    img.append(pygame.image.load(salida))                 # 3
    img.append(pygame.image.load(error))                  # 4
    img.append(pygame.image.load(background))             # 5
    img.append(pygame.image.load(main_screen_background)) # 6
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

def load_main_game():
    
    start = (2,3)
    end   = (11,33)
    
    fil = len(mapaBit)
    col = len(mapaBit[0])
    pygame.init()
    pygame.display.set_caption("Laberinto")
    pantalla = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    texturas = cargarImagenes()

    path = None

    clock = pygame.time.Clock()

    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
        pantalla.blit(texturas[5], [0,0], (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))  #cancha
        
        
        mapaDibujo(fil,col,mapaBit,pantalla,texturas,TAM_TEXTURA) #Texturas
        if path is None:
            path = a_algorit(mapaBit,start,end,pantalla)
            print(path)
            for position in reversed(path):
                clock.tick(60)
                #time.sleep(0.1)
                caminarPersonaje(len(mapaBit),len(mapaBit[0]),mapaBit,pantalla,cargarImagenes(),40,position)
                pygame.display.update()

    
        #pygame.display.update()

def load_main_screen():
    #Inicializar Pygame
    pygame.init()

    #Establecer titulo del juego
    pygame.display.set_caption("FIFA 1980")

    #Establecer la Pantalla Principal
    pantalla = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    #Cargar imagenes
    texturas = cargarImagenes()

    #Establecer tiempo para cargar frames por segundo
    clock = pygame.time.Clock()

    #Establecer las fuentes
    title_font = pygame.font.SysFont(None, 72)
    subtitle_font = pygame.font.SysFont(None, 36)

    #Titulo
    title = title_font.render('FIFA 1980', True, (255, 0, 0), (255, 255, 255))
    title_rect = title.get_rect()
    title_rect.centerx = pantalla.get_rect().centerx
    title_rect.centery = pantalla.get_rect().centery - 80

    #Comenzar Juego
    start_game = subtitle_font.render('Comenzar Juego', True, (255, 0, 0), (255, 255, 255))
    start_game_rect = start_game.get_rect()
    start_game_rect.centerx = pantalla.get_rect().centerx
    start_game_rect.centery = pantalla.get_rect().centery

    #Personalizar Campo
    customize_game = subtitle_font.render('Personalizar Campo', True, (255, 0, 0), (255, 255, 255))
    customize_game_rect = customize_game.get_rect()
    customize_game_rect.centerx = pantalla.get_rect().centerx
    customize_game_rect.centery = pantalla.get_rect().centery + 80

    #Menu Principal
    back_title = subtitle_font.render('Menu Principal', True, (255, 0, 0), (255, 255, 255))
    back_title_rect = back_title.get_rect()
    back_title_rect.centerx = 120
    back_title_rect.centery = 40

    #Salir - Menu Principal
    main_quit = subtitle_font.render('Salir', True, (255, 0, 0), (255, 255, 255))
    main_quit_rect = main_quit.get_rect()
    main_quit_rect.centerx = pantalla.get_rect().centerx
    main_quit_rect.centery = pantalla.get_rect().centery + 160

    #Guardar ruta recorrida
    path = None

    #El juego comienza
    gameStarted = False

    #Cantidad de filas
    fil = len(mapaBit)

    #Cantidad de columnas
    col = len(mapaBit[0])

    #Punto de Inicio
    start = (2,3)

    #Punto de Meta
    end   = (11,33)

    while True:
        clock.tick(60)

        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                if start_game_rect.collidepoint(eventos.pos):
                    gameStarted = True
                elif customize_game_rect.collidepoint(eventos.pos):
                    print ("Personalizar el juego")
                elif main_quit_rect.collidepoint(eventos.pos):
                    exit()
                elif gameStarted and back_title_rect.collidepoint(eventos.pos):
                    gameStarted = False

        if gameStarted:
            position = (0, 0)
            #Precalcular ruta del juego
            if path is None:
                path = a_algorit(mapaBit,start,end,pantalla)
            elif path is not None and len(path) > 0:
                position = path.pop()
                print(position)

            #Dibujar Campo
            pantalla.blit(texturas[5], [0,0], (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))  #cancha

            #Dibujar elementos del campo
            mapaDibujo(fil,col,mapaBit,pantalla,texturas,TAM_TEXTURA) #Texturas

            #Dibujar opcion para volver al menu principal
            pantalla.blit(back_title, back_title_rect)

            #Dibujar movimiento del jugador
            if len(path) > 0:
                caminarPersonaje(len(mapaBit),len(mapaBit[0]),mapaBit,pantalla,cargarImagenes(),40,position)
        else:
            #Dibujar Fondo Principal
            pantalla.blit(texturas[6], [0,0], (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))  #pantalla principal

            #Dibujar titulo
            pantalla.blit(title, title_rect)

            #Dibujar Comenzar Juego
            pantalla.blit(start_game, start_game_rect)

            #Dibujar Personalizar Campo
            pantalla.blit(customize_game, customize_game_rect)

            #Dibujar Salir de juego
            pantalla.blit(main_quit, main_quit_rect)
            

        pygame.display.update()

if __name__ == '__main__':
    load_main_screen()