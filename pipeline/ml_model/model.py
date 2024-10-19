from sklearn.linear_model import LinearRegression

# Função para treinar um modelo de regressão linear
def train_linear_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

# Função para fazer previsões com um modelo treinado
def predict(model, X):
    return model.predict(X)