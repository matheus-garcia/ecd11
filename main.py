import pandas as pd
from pipeline.preprocess.preprocess_data import normalize_column, fill_missing_values
from pipeline.ml_model.model import train_linear_model, predict
import sys

def main(csv_file_path):
    # Passo 1: Carregar os dados do CSV em um DataFrame
    df = pd.read_csv(csv_file_path)
    print(f"Dados carregados:\n{df.head()}")

    # Passo 2: Pré-processamento
    df = fill_missing_values(df, 'value')  # Preencher valores ausentes
    df = normalize_column(df, 'value')  # Normalizar coluna
    print(f"Dados após pré-processamento:\n{df.head()}")

    # Passo 3: Separar X e y para o modelo
    X = df[['value']]  # Exemplo: usar a coluna 'value' como X
    y = df['target']  # Exemplo: assumir que você tem uma coluna 'target'
    
    # Passo 4: Treinar o modelo
    model = train_linear_model(X, y)
    print(f"Modelo treinado.")

    # Passo 5: Fazer previsões
    predictions = predict(model, X)
    print(f"Previsões:\n{predictions}")

if __name__ == "__main__":
    # O caminho do arquivo CSV é passado como argumento ao script
    if len(sys.argv) != 2:
        print("Uso: python main.py <caminho_para_o_csv>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    main(csv_file_path)
