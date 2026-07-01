from rich import print
from collections.abc import Callable
from utils.inputs import pedir_texto_no_vacío
from typing import Any
from .core.exceptions import ComandoSalirException

#===================================================Matrices===================================================
def construir_matriz(filas: int = 1, columnas: int = 1, 
                     función_usada: Callable = pedir_texto_no_vacío, 
                     *args, **kwargs) -> list[list]:
    '''Ejemplos rápidos:\n
    matriz = construir_matriz(2, 2, pedir_decimal_rango, mínimo=1.0, máximo=7.0)\n
    matriz = construir_matriz(2, 2, lambda X: pedir_decimal_rango('Hola', mínimo=0.0, máximo=5.0))
    '''
    matriz: list[list] = []

    for fila in range(filas):
        matriz.append([])
        for j in range(columnas):
            mensaje_base = f'Ingrese el {j + 1}° valor de la {fila + 1}° fila'
            
            valor = función_usada(mensaje_base, *args, **kwargs)
            matriz[fila].append(valor)
            
    return matriz

def mostrar_valor_matriz(matriz: list[list[Any]] | None = None, x: int = 1, y: int = 1) -> Any:
    '''Muestra lo que contiene una Matriz en un punto'''
    if matriz is None:
        print('[red]ERROR: Matriz no válida o inexistente.[/red]')
        return
    return matriz[y - 1][x - 1]

def reemplazar_valor_matriz(matriz: list[list[Any]] | None = None,
                     x: int = 1, 
                     y: int = 1,
                     reemplazo: Any = None,
                     función_usada: Callable = pedir_texto_no_vacío,
                     *args, **kwargs) -> None:
    """
    Reemplaza un valor en una matriz (basada en coordenadas 1-en-adelante).
    
    Ejemplos de uso correctos:
    1. Pasando los argumentos directos para la función recolectora:
       reemplazar_valor(matriz, 2, 2, función_usada=pedir_decimal_rango, mínimo=0.0, máximo=20.0)
       
    2. Usando una función lambda sin argumentos si prefieres preconfigurarla:
       reemplazar_valor(matriz, 2, 2, función_usada=lambda: pedir_decimal_rango('Hola', mínimo=0.0, máximo=20.0))
    """

    if matriz is None:
        print('[red]ERROR: Matriz [bold]inválida[/bold] o [bold]inexistente[/bold][/red]')
        return
        
    if (y < 1 or y > len(matriz)) or (x < 1 or x > len(matriz[0])):
        print('[red]ERROR: Posición fuera de rango.[/red]')
        return

    if reemplazo is None:
        try:
            reemplazo = función_usada(*args, **kwargs)
        except TypeError:
            print('[red]ERROR: Reemplazo [bold]inexistente[/bold] o argumentos de función inválidos.[/red]')
            return

    matriz[y - 1][x - 1] = reemplazo

def imprimir_matriz(matriz: list[list[Any]] | None = None) -> None:
    '''Imprime lo que contiene una Matriz.'''
    if matriz is None:
        print('[red]ERROR: Matriz no válida o inexistente.[/red]')
        return
    for i in matriz:
        print(i)

#====================================================Listas====================================================
def añadir_datos_lista(lista: list[Any] = None,
                       función_usada: Callable = pedir_texto_no_vacío,
                       *args, **kwargs) -> None:

    if lista is None:
        print('[red]ERROR: Lista no válida o inexistente.[/red]')
        return
    
    while True:
        try:
            dato_ingresado: str = función_usada(*args, **kwargs)
            lista.append(dato_ingresado)
        except ComandoSalirException:
            return