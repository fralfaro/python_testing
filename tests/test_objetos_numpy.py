import pytest
import numpy as np

from pytdd.objetos_numpy import mae, mape, reemplazar_por_promedio


@pytest.mark.parametrize(
    "targets,predictions, expected",
    [
        (np.array([0, 0, 0, 0, 0]), np.array([0, 0, 0, 0, 0]), 0),
        (np.array([1, 2, 3, 4, 5]), np.array([1.5, 1.5, 1.5, 1.5, 1.5]), 1.7),
    ],
)
def test_mae(targets, predictions, expected):
    result = mae(targets, predictions)
    assert result == expected


@pytest.mark.parametrize(
    "targets,predictions, expected",
    [
        (np.array([0, 0, 0, 0, 0]), np.array([0, 0, 0, 0, 0]), np.inf),
        (np.array([1, 2, 3, 4, 5]), np.array([1.5, 1.5, 1.5, 1.5, 1.5]), 0.515),
    ],
)
def test_mape(targets, predictions, expected):
    result = mape(targets, predictions)
    assert result == expected


@pytest.mark.parametrize(
    "arreglo, expected",
    [
        (np.array([0, 0, 0, 0, 0]), np.array([0, 0, 0, 0, 0])),
        (
            np.array([1.0, 2, 3, 4, 5, 6, 0, 0, 0, 0]),
            np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 3.5, 3.5, 3.5, 3.5]),
        ),
    ],
)
def test_reemplazar_por_promedio(arreglo, expected):
    result = reemplazar_por_promedio(arreglo)
    np.testing.assert_array_equal(result, expected)
