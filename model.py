from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import categorical_crossentropy


def createModel(learning_rate=0.001):
    assert learning_rate != 0

    model = Sequential(
        [
            Dense(units=9, activation='tanh', input_shape=(9,), name='INPUT'),
            Dense(units=12, activation='tanh'),
            Dense(units=10, activation='tanh'),
            Dense(units=3, activation='softmax', name='OUTPUT')
        ]
    )
    model.compile(Adam(learning_rate=learning_rate), loss=categorical_crossentropy, metrics=['accuracy'])
    model.summary()

    return model
