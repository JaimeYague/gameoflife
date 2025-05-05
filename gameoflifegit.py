#raquel
import os
import random
import time

print(os.get_terminal_size())


def cuadricula():
    filas = os.get_terminal_size().lines
    columnas = os.get_terminal_size().columns
    tablero = [[random.randint(0, 1) for _ in range(columnas)] for _ in range(filas)]
    return tablero

def contarvecinos(tablero, fila, columna):
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinos_vivos = 0
    
    for i in range(fila - 1, fila + 2):
        for j in range(columna - 1, columna + 2):
            if i == fila and j == columna:
                continue

            if 0 <= i < filas and 0 <= j < columnas:
                vecinos_vivos += tablero[i][j]

    return vecinos_vivos


def siguiente_generacion(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            vecinos = contarvecinos(tablero, i, j)
            celda = tablero[i][j]

            # Reglas del Juego de la Vida
            if celda == 1:
                if vecinos == 2 or vecinos == 3:
                    nuevo_tablero[i][j] = 1  # sobrevive
                else:
                    nuevo_tablero[i][j] = 0  # muere
            else:
                if vecinos == 3:
                    nuevo_tablero[i][j] = 1  # nace
                else:
                    nuevo_tablero[i][j] = 0  # sigue muerta

    return nuevo_tablero


tablero = cuadricula()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # limpia pantalla
    for fila in tablero:
        print("".join("█" if celda else " " for celda in fila))
    tablero = siguiente_generacion(tablero)
    time.sleep(0.5)



    




                
