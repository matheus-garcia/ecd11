import pandas as pd

# Função para normalizar uma coluna de um DataFrame
def normalize_column(df, column_name):
    max_value = df[column_name].max()
    min_value = df[column_name].min()
    df[column_name] = (df[column_name] - min_value) / (max_value - min_value)
    return df

# Função para preencher valores ausentes com a média da coluna
def fill_missing_values(df, column_name):
    mean_value = df[column_name].mean()
    df[column_name].fillna(mean_value, inplace=True)
    return df