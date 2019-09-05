class nodo():
    def __init__(self,padre=None,pos=None):
        self.padre = padre
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0

def a_algorit(matriz,pos_ini,pos_final):
    #Listas
    L_Abiertas = []
    L_Cerradas = []
    print(pos_ini)
    #Nodo inicio y fin
    N_inicio = nodo(None,pos_ini)
    N_Fin = nodo(None,pos_final)

    L_Abiertas.append(pos_ini)

    while len(L_Abiertas) > 0:
        nodo_actual = L_Abiertas[0]
        print(nodo_actual.pos)
        actual_idnx = 0
        for index, item in enumerate(L_Abiertas):
            if item.f < nodo_actual.f:
                nodo_actual = item
                actual_idnx = index

        print(nodo_actual.pos)

            
        


def main():
    mapa = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] 
    
    start = (0,0)
    end = (6,8)
    print(start)
    a_algorit(mapa,start,end)
