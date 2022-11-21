import pandas as pd

def aplicar_funcion_collatz(df:pd.DataFrame)->pd.DataFrame:
    """
    Crea una nueva columna al dataframe llamada 'collatz'.
    (3n+1 si n es impar, n/2 si n es par)

    :param df: pandas DataFrame
        Index:
            RangeIndex
        Columns:
            Name: Integer, dtype: int64
            Name: Integer, dtype: int64
    :return: nuevo dataframe con la columna 'collatz'
    """

    df['collatz'] = df['numero'].apply(lambda x: 3*x+1 if x%2!=0 else x/2)

    return df