import matplotlib.pyplot as plt

def generate_line_chart(x, y):
  # Crear el gráfico de líneas
  plt.plot(x, y)

# Agregar etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de poblacion de un País')

# Mostrar el gráfico
plt.show()