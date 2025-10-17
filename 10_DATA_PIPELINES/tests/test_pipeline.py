import pytest
import pandas as pd
from ..transforms.transform_standard import standard_transform

def test_standard_transform():
    """
    Testa a função de transformação padrão.
    """
    data = {'col1': [1, 2, 3, 1, 5], 'col2': [10, 20, None, 10, 50]}
    df = pd.DataFrame(data)
    
    df_transformed = standard_transform(df.copy())
    
    # Verifica se não há mais valores nulos
    assert df_transformed.isnull().sum().sum() == 0
    
    # Verifica se as duplicadas foram removidas
    assert len(df_transformed) == 4
