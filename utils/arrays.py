from rich import print
from collections.abc import Callable
from utils.inputs import pedir_texto_no_vacío

def construir_matriz(filas: int = 1, columnas: int = 1, 
                     función_usada: Callable = pedir_texto_no_vacío, mensaje: str = None,
                     *args, **kwargs) -> list[list]:
    matriz: list[list] = []

    for fila in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[fila].append(función_usada(f'Ingrese el {j + 1}° valor de la {fila + 1}° fila'))
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