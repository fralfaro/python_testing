def sumar_dos_numeros(numero_1: float, numero_2: float) -> float:

    """
    Operacion 'sumar' de dos numeros reales.

    :param numero_1: numero real
    :param numero_2: numero real
    :return: suma de los dos numeros objetivos
    """

    return numero_1 + numero_2


def maximo_lista(lista: list) -> float:
    """
    Encontrar el valor maximo de una lista
    de valores numericos.

    :param lista: lista con valores numericos
    :return: valor maximo de la lista
    """

    if lista == []:
        result = 0
    else:
        result = max(lista)

    return result
