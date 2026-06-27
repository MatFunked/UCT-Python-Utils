from rich import print
from collections.abc import Callable
from utils.inputs import pedir_texto_no_vacío

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


def reemplazar_valor(matriz: list[list] = None, x: int = 1, y: int = 1, reemplazo = None,
                         función_usada: function = pedir_texto_no_vacío) -> None:
    reemplazo = función_usada if reemplazo is None else reemplazo
    matriz[y - 1][x - 1] = reemplazo


def añadir_datos(lista: list[float], mensaje: str = 'Ingrese un dato') -> None:
    MÉTODOS_SALIDA: tuple[str] = ('salir', 'exit')
    while True:
        entrada: str = pedir_texto_no_vacío(mensaje)
        if entrada in MÉTODOS_SALIDA:
            print()
            break
        try:
            tiempo_ingresado: float = float(entrada)
            lista.append(tiempo_ingresado)
        except ValueError:
            print(f'[red]ERROR: Input no admitido.[/red]\n')