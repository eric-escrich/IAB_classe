# Apuntes sobre Distribuciones y Test de Hipótesis

## 1. Tipos de Distribuciones
Las distribuciones de probabilidad pueden clasificarse en:

### a) Distribuciones Discretas
Las variables toman valores enteros específicos.
- **Distribución Binomial**: Modela el número de éxitos en una serie de ensayos de Bernoulli.
  - **PMF** (Función de Masa de Probabilidad): Probabilidad de obtener exactamente un número de éxitos.
  - **CDF** (Función de Distribución Acumulada): Probabilidad de que una variable tome un valor menor o igual a un valor dado.
  - **RVS** (Generador de Variables Aleatorias): Genera valores aleatorios siguiendo esta distribución.
- **Distribución de Poisson**: Modela la cantidad de eventos en un intervalo de tiempo o espacio.
  - Apropiada para eventos raros con tasa constante.
  - **PMF** y **CDF** similares a la binomial.
  - **RVS** permite simular eventos aleatorios.

### b) Distribuciones Continuas
Las variables pueden tomar cualquier valor dentro de un rango.
- **Distribución Normal**: Describen fenómenos naturales y tienen forma de campana.
  - **CDF** (Función de Distribución Acumulada): Probabilidad de que una variable sea menor o igual a un valor dado.
  - **PPF** (Percent Point Function): Inversa de la CDF, útil para calcular percentiles.
  - **RVS**: Genera valores aleatorios según la distribución normal.
- **Distribución Exponencial**: Modela los tiempos entre eventos en un proceso de Poisson.
  - Describe intervalos de tiempo entre eventos sucesivos.
  - **CDF** y **RVS** se utilizan para cálculos probabilísticos y simulaciones.

## 2. Detección de Tipo de Variable
- **Variable Continua**: Puede tomar valores con decimales (Ejemplo: Normal, Exponencial).
- **Variable Discreta**: Solo toma valores enteros (Ejemplo: Binomial, Poisson).

## 3. Test de Hipótesis
El **test de hipótesis** permite evaluar afirmaciones sobre una población en función de una muestra. Se usa principalmente en variables que siguen una distribución normal.

### a) Tipos de Pruebas
- **Muestras Independientes**: Se comparan dos grupos no relacionados.
- **Muestras Relacionadas**: Se comparan mediciones de la misma persona u objeto en diferentes condiciones.
  - Ejemplo: Comparar la media de una persona antes y después de un tratamiento.

### b) Prueba t de Student
Utilizada para comparar medias entre dos grupos:
- **t-test para muestras independientes**: Compara las medias de dos grupos distintos.
- **t-test para muestras relacionadas (pareadas)**: Compara la media de un mismo grupo en dos momentos distintos.

Este es un esquema general de las distribuciones y los test de hipótesis esenciales en estadística.

