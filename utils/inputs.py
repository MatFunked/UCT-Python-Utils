from rich import print
from utils.core.exceptions import ComandoSalirException
from utils.core.constants import MÉTODOS_SALIDA

#=====================================================Enteros=====================================================
def pedir_entero(mensaje: str = 'Ingrese un entero', *, marcador: bool = True) -> int:
    while True:
        if marcador:
            entrada_cruda: str = input(f'{mensaje}:\n > ')
        else:
            entrada_cruda: str = input(mensaje)

        if entrada_cruda.strip().lower() in MÉTODOS_SALIDA:
            raise ComandoSalirException()

        try:
            return int(entrada_cruda)
        except ValueError:
            print('[red]ERROR: Solo enteros admitidos.[/red]')

def pedir_entero_rango(mensaje: str = 'Ingrese un entero', *, mínimo: int = 0, máximo: int = 1,
                       marcador: bool = True, ) -> int:
    while True:
        número:int = pedir_entero(mensaje, marcador=marcador)
        if mínimo <= número <= máximo:
            return número
        else:
            print(f'[red]ERROR: Ingrese un entero entre {mínimo} y {máximo}.[/red]')

def pedir_entero_positivo(mensaje: str = 'Ingrese un entero positivo', *, incluir_cero: bool = True,
                          marcador: bool = True) -> int:
    límite: int = 0 if incluir_cero else 1
    while True:
        número: int = pedir_entero(mensaje, marcador=marcador)
        if número >= límite:
            return número
        print(f'[red]ERROR: Ingrese un entero positivo.[/red]')

def pedir_ciertos_enteros(cantidad: int = 1) -> list[int]:
    números:list[int] = []
    for i in range(cantidad):
        números.append(pedir_entero(f'Ingrese el {i + 1}° número'))
    return números

#====================================================Decimales====================================================
def pedir_decimal(mensaje:str='Ingrese un decimal', *, marcador:bool=True) -> float:
    while True:
        if marcador:
            entrada_cruda: str = input(f'{mensaje}:\n > ')
        else:
            entrada_cruda: str = input(mensaje)

        if entrada_cruda.strip().lower() in MÉTODOS_SALIDA:
            raise ComandoSalirException()
        
        try:
            return float(entrada_cruda)
        except ValueError:
            print('[red]ERROR: Solo decimales admitidos.[/red]')

def pedir_decimal_rango(mensaje: str = 'Ingrese un decimal', *, marcador: bool = True,
                        mínimo: float = 0.0, máximo: float = 1.0) -> float:
    while True:
        número:float = pedir_decimal(mensaje, marcador=marcador)
        if mínimo <= número <= máximo:
            return número
        else:
            print(f'[red]ERROR: Ingrese un número entre {mínimo} y {máximo}.[/red]')

def pedir_decimal_positivo(mensaje: str = 'Ingrese un decimal positivo', *, incluir_cero: bool = True,
                          marcador: bool = True) -> float:
    límite: float = 0 if incluir_cero else 1
    while True:
        número: float = pedir_decimal(mensaje, marcador=marcador)
        if número >= límite:
            return número
        print(f'[red]ERROR: Ingrese un decimal positivo.[/red]')

def pedir_ciertos_decimales(cantidad: int = 1) -> list[float]:
    números:list[float] = []
    for i in range(cantidad):
        números.append(pedir_decimal(f'Ingrese el {i + 1}° número'))
    return números

#=====================================================Strings=====================================================
def pedir_texto_no_vacío(mensaje: str = 'Ingrese un texto no vacío', *, marcador: bool = True) -> str:
    while True:
        texto: str = input(f'{mensaje}\n > ') if marcador else input(mensaje)
        if texto and not texto.isspace():
            return texto
        print('[red]ERROR: Este campo no puede estar vacío.[/red]')
    
def pedir_caracter(mensaje: str = 'Ingrese un caracter', *, marcador: bool = True) -> str:
    while True:
        texto: str = pedir_texto_no_vacío(mensaje, marcador=marcador)
        if len(texto) == 1:
            return texto
        print('[red]ERROR: Solo un caracter a la vez.[/red]')

#====================================================Booleanos====================================================
def pedir_booleano(mensaje: str = 'Confirma? (s/n)', *, marcador: bool = True) -> bool:
    '''Confirmación de (Sí/No)'''
    while True:
        entrada: str = pedir_texto_no_vacío(mensaje, marcador=marcador).strip().lower()
        match entrada:
            case 'si'|'sí'|'y'|'yes'|'s':
                return True
            case 'no'|'not'|'n':
                return False
            case _:
                print('[red]ERROR: Solo confirmación (s/n) admitida.[/red]')
