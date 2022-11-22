import pytest
from pytdd.objetos_python import sumar_dos_numeros, maximo_lista


@pytest.mark.parametrize("numero_1,numero_2, expected", [(1, 1, 2), (1, 2, 3)])
def test_sumar_dos_numeros(numero_1, numero_2, expected):
    result = sumar_dos_numeros(numero_1, numero_2)
    assert result == expected


@pytest.mark.parametrize(
    "lista, expected", [([1, 1, 1, 1, 1, 1, 1, 1, 2], 2), ([1, 4, 5, 6, 6], 6), ([], 0)]
)
def test_maximo_lista(lista, expected):
    result = maximo_lista(lista)
    assert result == expected
