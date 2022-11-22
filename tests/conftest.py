import pandas as pd
import pytest
from pathlib import Path


@pytest.fixture(name="df_file_csv")
def dataframe_file():
    path = Path("./tests/dataframe_file.csv")
    assert path.exists()
    return path


@pytest.fixture(name="df_obj")
def dataframe_obj():
    return pd.DataFrame(
        {
            "id": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            "numero": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "collatz": [4.0, 1.0, 10.0, 2.0, 16.0, 3.0, 22.0, 4.0, 28.0, 5.0],
        }
    )
