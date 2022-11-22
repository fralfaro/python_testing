# Pytest

## Introducción

El framework [pytest](https://docs.pytest.org/en/stable/) facilita la
escritura de pequeños tests, pero escala para admitir test funcionales
complejas para aplicaciones y librerias.

Si ha escrito pruebas unitarias para su código Python antes, es posible
que haya utilizado el módulo `unittest` integrado de Python. `unittest`
proporciona una base sólida sobre la cual construir su suite de pruebas,
pero tiene algunas deficiencias.

Varios marcos de prueba de terceros intentan abordar algunos de los
problemas con unittest, y pytest ha demostrado ser uno de los más
populares. pytest es un ecosistema basado en complementos y rico en
funciones para probar su código Python.


## Uso de Pytest

Si no se especifican argumentos, los archivos de tests se buscan en
ubicaciones desde las rutas de tests (si están configuradas) o el
directorio actual. Alternativamente, los argumentos de la línea de
comandos se pueden utilizar en cualquier combinación de directorios,
nombres de archivos o ID de nodo.

En los directorios seleccionados, pytest busca archivos de `test _ *.py`
o `*_test.py`. En los archivos seleccionados, pytest busca funciones de
test con prefijo test.



Veamos un ejemplo sencillo de esto:



**a) Escribir funciones a testear**


``` python
%%writefile algo.py
def max(values):
    _max = values[0]
    for val in values:
        if val > _max:
            _max = val

    return _max


def min(values):
    _min = values[0]

    for val in values:
        if val < _min:
            _min = val

    return _min
```







**b) Escribir los tests**


``` python
%%writefile test_min_max.py
import algo

def test_min():
    values = (2, 3, 1, 4, 6)

    val = algo.min(values)
    assert val == 1

def test_max():
    values = (2, 3, 1, 4, 6)

    val = algo.max(values)
    assert val == 6
```






El archivo `test_min_max.py` tiene una palabra de **test** en su nombre.
Nos sirve para diferenciar entre un script de python genérico respecto a
uno de testeo.


``` python
!pytest test_min_max.py
```



``` 
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
plugins: hypothesis-5.49.0, cov-2.11.1
collecting ... 
collected 2 items                                                              

test_min_max.py ..                                                       [100%]

============================== 2 passed in 0.02s ===============================
```







Esta es la salida. Hubo dos pruebas y ambas han pasado con éxito. Se
muestra una salida más detallada con `pytest -v test_min_max.py`.





## Pytest skip

Con el decorador de `skip`, podemos omitir los test especificados. Hay
varias razones para saltarse el test; por ejemplo, una base de
datos/servicio en línea no está disponible en este momento o nos
saltamos los test específicas de Linux en Windows.




``` python
%%writefile skipping.py
import algo
import pytest

@pytest.mark.skip
def test_min():
    values = (2, 3, 1, 4, 6)

    val = algo.min(values)
    assert val == 1

def test_max():
    values = (2, 3, 1, 4, 6)

    val = algo.max(values)
    assert val == 6
```









En el ejemplo, se omite `test_min()`.




``` python
!pytest skipping.py
```


    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
    rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
    plugins: hypothesis-5.49.0, cov-2.11.1
    collected 2 items                                                              
    
    skipping.py s.                                                           [100%]
    
    ========================= 1 passed, 1 skipped in 0.02s =========================







## Pytest Xfail

Podemos usar el marcador `xfail` para indicar que espera que falle una
prueba.

Un caso de uso común para esto es cuando encuentra un error en su
software y escribe una prueba para documentar cómo debería comportarse
el software. Esta prueba, por supuesto, fallará hasta que corrija el
error.

Para evitar tener una prueba fallida, marca la prueba como `xfail`. Una
vez que se corrige el error, elimina el marcador xfail y tiene una
prueba de regresión que asegura que el error no se repita.




``` python
%%writefile xfail.py
import pytest
xfail = pytest.mark.xfail

@xfail
def test_hello():
    assert 0

@xfail(run=False)
def test_hello2():
    assert 0

@xfail("hasattr(os, 'sep')")
def test_hello3():
    assert 0

@xfail(reason="bug 110")
def test_hello4():
    assert 0

@xfail('pytest.__version__[0] != "17"')
def test_hello5():
    assert 0

def test_hello6():
    pytest.xfail("reason")

@xfail(raises=IndexError)
def test_hello7():
    x = []
    x[1] = 1
```








En este caso, todos los test serán ignorados (con una **x**), lo cuál no
afectará al resto de los tests (suponiendo que los tests pasen
correctamente).




``` python
!pytest xfail.py
```


    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
    rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
    plugins: hypothesis-5.49.0, cov-2.11.1
    collected 7 items                                                              
    
    xfail.py xxxxxxx                                                         [100%]
    
    ============================== 7 xfailed in 0.13s ==============================







## Pytest marking

Podemos usar marcadores para organizar los test unitarios.




``` python
%%writefile marking.py
import pytest

@pytest.mark.a
def test_a1():

    assert (1) == (1)

@pytest.mark.a
def test_a2():

    assert (1, 2) == (1, 2)

@pytest.mark.a
def test_a3():

    assert (1, 2, 3) == (1, 2, 3)

@pytest.mark.b
def test_b1():

    assert "falcon" == "fal" + "con"

@pytest.mark.b
def test_b2():

    assert "falcon" == f"fal{'con'}"
```









Tenemos dos grupos de tests identificados por marcadores, \(a\) y \(b\).
Estas unidades son ejecutadas por `pytest -m a marking.py` y `pytest -m
b marking.py`.




``` python
!pytest -m a marking.py
```


``` 
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
plugins: hypothesis-5.49.0, cov-2.11.1
collecting ... 
collected 5 items / 2 deselected / 3 selected                                  

marking.py ...                                                           [100%]

=============================== warnings summary ===============================
marking.py:3
  /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing/marking.py:3: PytestUnknownMarkWarning: Unknown pytest.mark.a - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    @pytest.mark.a

marking.py:8
  /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing/marking.py:8: PytestUnknownMarkWarning: Unknown pytest.mark.a - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    @pytest.mark.a

marking.py:13
  /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing/marking.py:13: PytestUnknownMarkWarning: Unknown pytest.mark.a - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    @pytest.mark.a

marking.py:18
  /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing/marking.py:18: PytestUnknownMarkWarning: Unknown pytest.mark.b - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    @pytest.mark.b

marking.py:23
  /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing/marking.py:23: PytestUnknownMarkWarning: Unknown pytest.mark.b - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    @pytest.mark.b

-- Docs: https://docs.pytest.org/en/latest/warnings.html
================= 3 passed, 2 deselected, 5 warnings in 0.02s ==================
```






``` python
!pytest -m b marking.py
```


``` 
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
plugins: hypothesis-5.49.0, cov-2.11.1
collecting ... 
collected 5 items / 3 deselected / 2 selected                                  

marking.py ..                                                            [100%]

=============================== warnings summary ===============================
marking.py:3
  /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing/marking.py:3: PytestUnknownMarkWarning: Unknown pytest.mark.a - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    @pytest.mark.a

marking.py:8
  /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing/marking.py:8: PytestUnknownMarkWarning: Unknown pytest.mark.a - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    @pytest.mark.a

marking.py:13
  /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing/marking.py:13: PytestUnknownMarkWarning: Unknown pytest.mark.a - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    @pytest.mark.a

marking.py:18
  /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing/marking.py:18: PytestUnknownMarkWarning: Unknown pytest.mark.b - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    @pytest.mark.b

marking.py:23
  /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing/marking.py:23: PytestUnknownMarkWarning: Unknown pytest.mark.b - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    @pytest.mark.b

-- Docs: https://docs.pytest.org/en/latest/warnings.html
================= 2 passed, 3 deselected, 5 warnings in 0.02s ==================
```







## Pytest parameterized tests

Con los tests parametrizados, podemos agregar múltiples valores a
nuestras afirmaciones. Usamos el decorador `@pytest.mark.parametrize`.




``` python
%%writefile parameterized.py
import algo
import pytest

@pytest.mark.parametrize("data, expected", [((2, 3, 1, 4, 6), 1), 
    ((5, -2, 0, 9, 12), -2), ((200, 100, 0, 300, 400), 0)])
def test_min(data, expected):

    val = algo.min(data)
    assert val == expected

@pytest.mark.parametrize("data, expected", [((2, 3, 1, 4, 6), 6), 
    ((5, -2, 0, 9, 12), 12), ((200, 100, 0, 300, 400), 400)])
def test_max(data, expected):

    val = algo.max(data)
    assert val == expected
```








Pasamos dos valores a la función de testeo: los datos y el valor
esperado. En nuestro caso, probamos la función `min()` con tres tuplas
de datos.




``` python
!pytest parameterized.py
```


    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
    rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
    plugins: hypothesis-5.49.0, cov-2.11.1
    collected 6 items                                                              
    
    parameterized.py ......                                                  [100%]
    
    ============================== 6 passed in 0.03s ===============================







## Pytest fixtures

Los tests deben ejecutarse en el contexto de un conjunto conocido de
objetos. Este conjunto de objetos se denomina `test fixture`.




``` python
%%writefile algo2.py
def sel_sort(data):
    if not isinstance(data, list):
        vals = list(data)
    else:
        vals = data

    size = len(vals)

    for i in range(0, size):

        for j in range(i+1, size):

            if vals[j] < vals[i]:
                _min = vals[j]
                vals[j] = vals[i]
                vals[i] = _min
    return vals
```








``` python
%%writefile fixtures.py

import algo2
import pytest

# fijar valor data
@pytest.fixture
def data():
    return [3, 2, 1, 5, -3, 2, 0, -2, 11, 9]

# pasar data como argumento del test
def test_sel_sort(data):
    sorted_vals = algo2.sel_sort(data)
    assert sorted_vals == sorted(data)
```








``` python
!pytest fixtures.py
```


``` 
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
plugins: hypothesis-5.49.0, cov-2.11.1
collecting ... 
collected 1 item                                                               

fixtures.py .                                                            [100%]

============================== 1 passed in 0.02s ===============================
```







**Observación**: para realizar los siguientes ejemplos, es necesario
eliminar todos los archivos `.py` previos.




``` python
# eliminar archivos .py
!rm *.py
```





## Pytest layouts

Los tests de Python se pueden organizar de varias formas. Los tests se
pueden integrar en el paquete de Python o pueden descansar fuera de la
librería.





### Integrated tests

A continuación, mostramos cómo ejecutar pruebas dentro de un paquete de
Python.

``` terminal
setup.py
utils
│   algo.py
│   srel.py
│   __init__.py
│
└───tests
        algo_test.py
        srel_test.py
        __init__.py
```





Tenemos este diseño del paquete. Los test se encuentran en el
subdirectorio de **tests** dentro del paquete.





### a) crear archivos previos del ejemplos




``` python
# crear carpetas
!mkdir utils tests
```




``` python
# agregar archivo __init__.py
!touch utils/__init__.py 
```




``` python
# agregar archivo __init__.py
!touch tests/__init__.py
```





### b) crear archivos .py a testear




``` python
%%writefile setup.py
from setuptools import setup, find_packages
setup(name="utils", packages=find_packages())
```







``` python
%%writefile utils/algo.py
def sel_sort(data):
    if not isinstance(data, list):
        vals = list(data)
    else:
        vals = data

    size = len(vals)

    for i in range(0, size):

        for j in range(i+1, size):

            if vals[j] < vals[i]:
                _min = vals[j]
                vals[j] = vals[i]
                vals[i] = _min
    return vals

def max(values):
    _max = values[0]
    for val in values:
        if val > _max:
            _max = val

    return _max


def min(values):
    _min = values[0]

    for val in values:
        if val < _min:
            _min = val

    return _min
```



``` python
%%writefile utils/srel.py

def is_palindrome(val):
    return val == val[::-1]
```







### c) crear los tests


``` python
%%writefile tests/algo_test.py
import utils.algo
import pytest

@pytest.mark.parametrize(
    "data",
    [
        [3, 2, 1, 5, -3, 2, 0, -2, 11, 9],
        (3, 2, 1, 5, -3, 2, 0, -2, 11, 9)
    ]
)
def test_sel_sort(data):
    sorted_vals = utils.algo.sel_sort(data)
    assert sorted_vals == sorted(data)

@pytest.fixture
def values():
    return (2, 3, 1, 4, 6)

def test_min(values):
    val = utils.algo.min(values)
    assert val == 1

def test_max(values):
    val = utils.algo.max(values)
    assert val == 6
```







``` python
%%writefile tests/srel_test.py
import utils.srel
import pytest

@pytest.mark.parametrize(
    "word, expected", 
    [
        ('kayak', True), 
        ('civic', True), 
        ('forest', False)
    ]
)
def test_palindrome(word, expected):

    val = utils.srel.is_palindrome(word)
    assert val == expected
```


``` python
# dejar tests en la ruta correcta
!mv tests utils
```





### d) correr los test \!



``` python
!pytest --pyargs utils 
```


    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
    rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
    plugins: hypothesis-5.49.0, cov-2.11.1
    collected 7 items                                                              
    
    utils/tests/algo_test.py ....                                            [ 57%]
    utils/tests/srel_test.py ...                                             [100%]
    
    ============================== 7 passed in 0.04s ===============================







## Tests outside the package

El siguiente ejemplo muestra un diseño dela aplicación donde los tests
no están integrados dentro del paquete.





``` terminal
setup.py
src
└───utils
│       algo.py
│       srel.py
tests
    algo_test.py
    srel_test.py
```





En este diseño, tenemos tets fuera del árbol de fuentes.





### a) crear diseño del ejemplo




``` python
# crear carpeta src
!mkdir src
```




``` python
# mover carpeta utils
!mv utils  src
```




``` python
# mover carpeta tests
!mv src/utils/tests  src/
```





### b) Correr los test \!




``` python
!pytest
```


``` 
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
plugins: hypothesis-5.49.0, cov-2.11.1
collecting ... 
collected 7 items                                                              

src/tests/algo_test.py ....                                              [ 57%]
src/tests/srel_test.py ...                                               [100%]

============================== 7 passed in 0.04s ===============================
```



