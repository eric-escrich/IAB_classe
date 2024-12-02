# Importem les llibreries necessàries

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D


# Carreguem les dades de MNIST
from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# Fem el reshape de les dades i les normalitzem
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255


# Creació de la CNN
model = Sequential()
model.add(Conv2D(32, kernel_size=(5, 5), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, kernel_size=(5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(10, activation='softmax'))

model.summary()


# Visualització gràfica de la CNN
import visualkeras
visualkeras.layered_view(model, legend=True).show()

# Compilació i entrenament
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=15,batch_size=100)

test_loss, test_acc = model.evaluate(x_test, y_test)



# Generem prediccions
predictio = model.predict(x_test[111:112])
print(predictio)

print(predictio.round(2))

print('prediccio:', np.argmax(predictio))
print('resposta correcte', np.argmax(y_test[111]))


plt.imshow(x_test[11].reshape(28, 28), cmap=plt.cm.binary)
plt.show()

