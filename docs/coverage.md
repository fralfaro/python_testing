# Coverage

## Introducción

Este plugin produce informes de cobertura. En comparación con el uso de
`coverage run`, este complemento tiene algunos extras:

  - Soporte de subprocesos: puede bifurcar o ejecutar cosas en un
    subproceso y estará cubierto sin ningún problema.
  - Soporte de `Xdist`: puede usar todas las funciones de pytest-xdist y
    aún obtener cobertura.
  - Comportamiento constante de Pytest. Si ejecuta la sentencia
    `coverage run -m pytest`, tendrá `sys.path` ligeramente diferente
    (CWD estará en él, a diferencia de cuando se ejecuta `pytest`).


## Reporting

  - Es posible generar cualquier combinación de informes para una sola
    ejecución de test.
  - Los informes disponibles son terminales (con o sin los números de
    línea que faltan), HTML, XML y código fuente anotado.

Lo primero es replicar el ejemplo de la seción **Pytest**:



### Caso 01

El informe del terminal sin números de línea (default):


``` python
!pytest --cov-report term --cov=src
```



    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
    rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
    plugins: hypothesis-5.49.0, cov-2.11.1
    collected 7 items                                                              
    
    src/tests/algo_test.py ....                                              [ 57%]
    src/tests/srel_test.py ...                                               [100%]
    
    ----------- coverage: platform linux, python 3.8.5-final-0 -----------
    Name                     Stmts   Miss  Cover
    --------------------------------------------
    src/tests/__init__.py        0      0   100%
    src/tests/algo_test.py      15      0   100%
    src/tests/srel_test.py       6      0   100%
    src/utils/__init__.py        0      0   100%
    src/utils/algo.py           24      0   100%
    src/utils/srel.py            2      0   100%
    --------------------------------------------
    TOTAL                       47      0   100%
    
    
    ============================== 7 passed in 0.09s ===============================




### Caso 02

El informe de la terminal con números de línea:



``` python
!pytest --cov-report term-missing --cov=src
```


    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
    rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
    plugins: hypothesis-5.49.0, cov-2.11.1
    collected 7 items                                                              
    
    src/tests/algo_test.py ....                                              [ 57%]
    src/tests/srel_test.py ...                                               [100%]
    
    ----------- coverage: platform linux, python 3.8.5-final-0 -----------
    Name                     Stmts   Miss  Cover   Missing
    ------------------------------------------------------
    src/tests/__init__.py        0      0   100%
    src/tests/algo_test.py      15      0   100%
    src/tests/srel_test.py       6      0   100%
    src/utils/__init__.py        0      0   100%
    src/utils/algo.py           24      0   100%
    src/utils/srel.py            2      0   100%
    ------------------------------------------------------
    TOTAL                       47      0   100%
    
    
    ============================== 7 passed in 0.10s ===============================



### Caso 03

El informe de la terminal con `skip covered`:



``` python
!pytest --cov-report term:skip-covered --cov=src
```



    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
    rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
    plugins: hypothesis-5.49.0, cov-2.11.1
    collected 7 items                                                              
    
    src/tests/algo_test.py ....                                              [ 57%]
    src/tests/srel_test.py ...                                               [100%]
    
    ----------- coverage: platform linux, python 3.8.5-final-0 -----------
    Name    Stmts   Miss  Cover
    ---------------------------
    ---------------------------
    TOTAL      47      0   100%
    
    6 files skipped due to complete coverage.
    
    
    ============================== 7 passed in 0.10s ===============================



### Caso 04

Estas tres opciones de informe se envían a archivos sin mostrar nada
en el terminal:


``` python
!pytest --cov-report html \
        --cov-report xml \
        --cov-report annotate \
        --cov=src
```


    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
    rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
    plugins: hypothesis-5.49.0, cov-2.11.1
    collected 7 items                                                              
    
    src/tests/algo_test.py ....                                              [ 57%]
    src/tests/srel_test.py ...                                               [100%]
    
    ----------- coverage: platform linux, python 3.8.5-final-0 -----------
    Coverage annotated source written next to source
    Coverage HTML written to dir htmlcov
    Coverage XML written to file coverage.xml
    
    
    ============================== 7 passed in 0.15s ===============================



### Caso 05

Se puede especificar la ubicación de salida para cada uno de estos
informes. La ubicación de salida del informe XML es un archivo. Donde,
como ubicación de salida para los informes HTML y de código fuente
anotado son directorios:



``` python
! pytest --cov-report html:cov_html \
        --cov-report xml:cov.xml \
        --cov-report annotate:cov_annotate \
        --cov=src
```


    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
    rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
    plugins: hypothesis-5.49.0, cov-2.11.1
    collected 7 items                                                              
    
    src/tests/algo_test.py ....                                              [ 57%]
    src/tests/srel_test.py ...                                               [100%]
    
    ----------- coverage: platform linux, python 3.8.5-final-0 -----------
    Coverage annotated source written to dir cov_annotate
    Coverage HTML written to dir cov_html
    Coverage XML written to file cov.xml
    
    
    ============================== 7 passed in 0.17s ===============================



### Caso 06

La opción de informe final también puede suprimir la impresión en el
terminal:



``` python
!pytest --cov-report= --cov=src 
```


    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
    rootdir: /home/fralfaro/PycharmProjects/python_development_tools/python_development_tools/testing
    plugins: hypothesis-5.49.0, cov-2.11.1
    collected 7 items                                                              
    
    src/tests/algo_test.py ....                                              [ 57%]
    src/tests/srel_test.py ...                                               [100%]
    
    
    
    ============================== 7 passed in 0.12s ===============================



Este modo puede ser especialmente útil en servidores de integración
continua, donde se necesita un archivo de cobertura para el
procesamiento posterior, pero no es necesario ver un informe local. Por
ejemplo, las pruebas realizadas en `Travis-CI` podrían generar un
archivo `.coverage` para usar con `Coveralls`.


