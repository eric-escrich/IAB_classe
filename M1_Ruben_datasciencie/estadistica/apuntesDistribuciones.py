# Distribución Bionomial / bernoulli
# La distribución binomial es una distribución de probabilidad discreta que describe el número de éxitos en una secuencia de n ensayos independientes entre sí, con una probabilidad fija p de ocurrencia del éxito entre los ensayos.
# indica la probabilidad de tener k exitos en n intentos (binomial 0.5)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(40)

# generamos un array con el num intentos
num_intentos = 10
random_numbers = np.empty(num_intentos)

# simulamos el tiro de una moneda
for n in range(num_intentos):
    res = np.random.random()
    if res < 0.5:
        random_numbers[n] = 1
    else:
        random_numbers[n] = 0

pd.Series(random_numbers).hist()