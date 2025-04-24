
import os
import random

print(os.get_terminal_size())


def cuadricula():
    filas = 5
    columnas = 5
    tablero = [[random.randint(0, 1) for _ in range(columnas)] for _ in range(filas)]

    for fila in tablero:
        print(fila)
    
    return tablero

def contarvecinos(fila, columna):
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinos_vivos = 0
    
    for i in range(fila -1, fila +2):
        for j in range(columna -1, columna +2):
            if i == fila and j == columna:
                continue

            if 0 <= i < filas and 0 <= col < columnas:
                vecinos_vivos += tablero[i][j]

        return vecinos_vivos