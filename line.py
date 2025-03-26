import matplotlib.pyplot as plt
import matplotlib
from matplotlib import pyplot as plt
dir(plt)
help(plt.plot)
import matplotlib.pyplot as plt

# Datos para graficar
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Crear un gráfico de líneas
plt.plot(x, y)

# Mostrar el gráfico
plt.show()