import numpy as np


def mae(targets: np.ndarray, predictions: np.ndarray) -> float:
    """
    Calculo de la metrica: mean absolute error (MAE)
    :param targets: valor real
    :param predictions: valor estimado
    :return: valor de la metrica
    """
    error = predictions - targets
    return round(np.abs(error).mean(), 4)


def mape(targets: np.ndarray, predictions: np.ndarray) -> float:
    """
    Calculo de la metrica: mean absolute percentage error (MAPE)
    :param targets: valor real
    :param predictions: valor estimado
    :return: valor de la metrica
    """
    error = predictions - targets

    if any(x == 0 for x in targets):
        return np.inf
    else:
        return round(np.abs(error / targets).mean(), 4)


def reemplazar_por_promedio(arreglo: np.ndarray) -> np.ndarray:
    """
    Reemplazar valores iguales cero por el promedio del
    resto de valores

    :param arreglo: arreglo numpy
    :return: arreglo numpy sin ceros
    """

    arreglo_nuevo = arreglo[arreglo != 0]

    if len(arreglo_nuevo) == 0:
        return arreglo
    else:
        promedio = np.mean(arreglo_nuevo)
        arreglo[arreglo == 0] = promedio
        return arreglo
