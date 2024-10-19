import pandas as pd
from pipeline.preprocess.preprocess_data import normalize_column, fill_missing_values

# Testa a função de normalização
def test_normalize_column():
    data = {'value': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)
    normalized_df = normalize_column(df, 'value')
    
    assert normalized_df['value'].min() == 0
    assert normalized_df['value'].max() == 1

# Testa a função de preenchimento de valores ausentes
def test_fill_missing_values():
    data = {'value': [10, None, 30, None, 50]}
    df = pd.DataFrame(data)
    df_filled = fill_missing_values(df, 'value')
    
    assert df_filled['value'].isnull().sum() == 0
    assert df_filled['value'].iloc[1] == df['value'].mean()
