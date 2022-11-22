# Python Testing

[![YourActionName Actions Status](https://github.com/fralfaro/python_testing/actions/workflows/testing.yml/badge.svg)](https://github.com/fralfaro/python_testing/actions)
[![codecov](https://codecov.io/gh/fralfaro/python_testing/branch/main/graph/badge.svg)](https://codecov.io/gh/fralfaro/python_testing)
<a href="https://fralfaro.github.io/python_testing/"><img alt="Link a la Documentación" src="https://img.shields.io/badge/docs-link-brightgreen"></a>



<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/static--analysis-black%20flake8-black"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/testing-pytest-black"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/documentation-sphinx-black"></a>


Introducción al mundo del testing con python (TDD, pytest, coverage, etc.).

> **Nota**: La documentación del proyecto se encuentra en el siguiente [link](https://fralfaro.github.io/python_testing/).

## Descripción del repositorio

```
|
+---.github
|   \---workflows
|           testing.yml
|
\---docs
|   \--- images
|   |   coverage.md
|   |   index.md
|   |   intro.md
|   |   pytest.md
|
|
\---pytdd
|   |   __init__.py
|   |   objetos_numpy.py
|   |   objetos_pandas.py
|   |   objetos_python.py
|   |   sin_test.py
|
|
\---tests
|   |   __init__.py
|   |   conftest.py
|   |   dataframe_file.csv
|   |   test_objetos_numpy.py
|   |   test_objetos_pandas.py
|   |   test_objetos_python.py
|
|
|  .coveragerc
|  .flake8
|  .gitignore
|  .pre-commit-config.yaml
|  LICENSE
|  mkdocs.yml
|  poetry.lock
|  pyproject.toml
|  README.md
```

donde:

* `.github`: carpeta para generar el CI del proyecto.
* `docs`: carpeta donde se almacena la documentación del proyecto.
* `pytdd`: carpeta con los códigos del proyecto.
* `tests`: carpeta con los tests de los códigos del proyecto.
* `.coveragerc`: archivo que administra las excepciones del coverage.
* `.flake8`: archivo que administra las excepciones del Flake8.
* `.gitignore`: lugar donde se define los archivos a ignorar.
* `.pre-commit-config.yaml`: archivo que adminstra el Code Quality.
* `LICENSE`: licencia asociada al proyecto.
* `mkdocs.yml`: archivo que administra la documentación del proyecto.
* `poetry.lock`: archivo que administra las dependencias del proyecto.
* `pyproject.toml`: archivo que administra las dependencias del proyecto.