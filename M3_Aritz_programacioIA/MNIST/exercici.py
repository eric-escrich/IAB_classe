# importem llibreries
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout

# comprovem la versió de tensorflow
# print(tf.__version__)


# importem el dataset MNIST i el gruardem en arrays de NumPy
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# Revisem la forma i tipus de les dades
# print(x_train.shape)
# print(y_train.shape)
# print(x_train.dtype)
# print(y_train.dtype)


#Mostrem la info d'una única imatge
# print(x_train[0])
# print(y_train[0])


# Visualitzem la imatge
# plt.imshow(x_train[0], cmap=plt.cm.binary)
# plt.show()


## PRE-PROCESSAMENT DE LES DADES
# Normalitzem les imatges
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# print(x_train[0])
# print(x_train.dtype)


# Convertim les matrius 2D de 28x28 pixels a vectors 1D de mida 784
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# print(x_train.shape)
# print(x_test.shape)


# Convertim les etiquetes a vectors binaris
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

print(y_train[80])


# Definim el model de xarxa neuronal
model = Sequential()

# Afegim una capa de 10 neurones amb 784 entrades i funció d'activació sigmoid
model.add(Dense(128, input_shape=(784,), activation='relu'))

# Afegim una caoa de sortuda de 10 neurones amb funció d'activació softmax
model.add(Dense(10, activation='softmax'))

# Visualitzem l'estructura de la xarxa neuronal
model.summary()

# Inici de la fase d'entrenament
# loss: funció de pèrdua - calcula l'error que hem comés en la predicció (com més baix millor)
# categorical_crossentropy: funció de pèrdua per classificació multiclasse
# optimizer: algoritme d'optimització - un cop coneixem l'error que hem comés com actualitzem els pesos perque millori la predicció
# adam: algoritme d'optimització
# metrics: mètrica per avaluar el model - ens diu com de bé està funcionant el model
# accuracy: percentatge de prediccions correctes
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenem el model
# x_train: dades d'entrenament
# y_train: etiquetes d'entrenament
# epochs: nombre d'iteracions sobre el dataset
# batch_size: nombre de mostres per actualitzar els pesos
model.fit(x_train, y_train, epochs=50, batch_size=32)

# Evaluem el model
test_lost, test_accuracy = model.evaluate(x_test, y_test)
print('Precisió de test:', test_accuracy)

# Generem prediccions
predictio = model.predict(x_test[11:12])
print(predictio)

print(predictio.round(2))

print('prediccio:', np.argmax(predictio))
print('resposta correcte', np.argmax(y_test[11]))


plt.imshow(x_test[11].reshape(28, 28), cmap=plt.cm.binary)
plt.show()
