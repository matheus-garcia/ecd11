import numpy as np
from sklearn.linear_model import LinearRegression
from ..pipeline.ml_model.model import *

# Testa o treinamento do modelo
def test_train_linear_model():
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])
    model = train_linear_model(X, y)
    
    assert isinstance(model, LinearRegression)

# Testa a função de previsão
def test_predict():
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])
    model = train_linear_model(X, y)
    
    predictions = predict(model, X)
    np.testing.assert_array_almost_equal(predictions, y)
