import pandas as pd
from pandas._testing import assert_frame_equal
from pytdd.objetos_pandas import aplicar_funcion_collatz


def test_aplicar_funcion_collatz(df_file_csv, df_obj):
    df = pd.read_csv(df_file_csv)
    result = aplicar_funcion_collatz(df)
    assert_frame_equal(result, df_obj)
