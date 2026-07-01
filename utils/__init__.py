from .aesthetic import(
    título,
    separador,
    cargando,
    pausar
)
from .arrays import(
    construir_matriz,
    mostrar_valor_matriz,
    imprimir_matriz,
    reemplazar_valor_matriz,
    añadir_datos_lista
)

from .inputs import(
    # Enteros ==============================
    pedir_entero,
    pedir_entero_positivo,
    pedir_entero_rango,
    pedir_ciertos_enteros,

    # Decimales ============================
    pedir_decimal,
    pedir_decimal_positivo,
    pedir_decimal_rango,
    pedir_ciertos_decimales,

    # Strings ==============================
    pedir_texto_no_vacío,
    pedir_caracter,

    # Booleanos ============================
    pedir_booleano
)

__version__ = "3.0.0"
__author__ = "END_MATH"
__description__ = """
Usar inputs.py para entradas de usuario y aesthetic.py para cuestiones estéticas

TEXTO ROJO: Indica errores al usar una función, revisa que los datos ingresados sean los esperados.
TEXTO VERDE: Texto de debug que indica que una tarea de finalizó con éxito.
"""