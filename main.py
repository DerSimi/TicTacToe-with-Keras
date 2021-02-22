from TicTacToe.model import createModel
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv('test.csv').to_numpy()

    x = data[:, :9]
    y = data[:, 9]

    y = y.reshape(-1, 1)

    encoder = OneHotEncoder(sparse=False)
    y = encoder.fit_transform(y)

    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.20)
    print("y:", y)

    print(len(train_x), 'Trainingsdatensätze und ', len(test_x), 'Testdatensätze')

    model = createModel(0.001)

    model.fit(x, y, verbose=2, batch_size=10, epochs=200)

    print("Model wurde evaluiert, Trefferquote von:", model.evaluate(test_x, test_y)[1])
