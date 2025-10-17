# Exemplo de script de transformação de dados com pandas.
import pandas as pd

def standard_transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica transformações padrão em um DataFrame.
    - Remove duplicados
    - Preenche valores nulos (com a média da coluna)
    """
    df = df.drop_duplicates()
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].mean())
    return df

if __name__ == "__main__":
    data = {'col1': [1, 2, 3, 1, 5], 'col2': [10, 20, None, 10, 50]}
    df = pd.DataFrame(data)
    print("DataFrame Original:")
    print(df)
    df_transformed = standard_transform(df.copy())
    print("\nDataFrame Transformado:")
    print(df_transformed)
