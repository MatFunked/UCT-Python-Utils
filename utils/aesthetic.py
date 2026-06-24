from time import sleep

def título(mensaje: str = 'Título', *, mayúscula: bool = True, largo: int = 45, caracter: str = '=',
           caracter_central: str = ' ') -> None:
    '''La centralización se rompe con Rich, se añadirán colores cuando se solucione.'''
    texto: str = mensaje.upper() if mayúscula else mensaje
    print(caracter * largo)
    print(texto.center(largo, caracter_central))
    print(caracter * largo)

def separador(mensaje: str = '', largo: int = 45, caracter: str = '-') -> None:
    if mensaje:
        print(f' {mensaje} '.center(largo, caracter))
    else:
        print(caracter * largo)

def cargando(mensaje: str = 'Cargando', *, ciclos: int = 10, espera: float = 0.3) -> None:
    '''"Cargando..." funcional.'''
    for i in range(ciclos):
        for j in range(4):
            print(f'{mensaje}{"."*j}', end='\r')
            sleep(espera)
    print(f'{mensaje}   ', end='\r')

def pausar(mensaje: str = 'Presione Enter para continuar...') -> None:
    input(mensaje)
