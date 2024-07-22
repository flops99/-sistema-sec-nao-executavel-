import matplotlib.pyplot as plt
import numpy as np

# Cria dados para o eixo x
x = np.linspace(0, 2 * np.pi, 100)

# Calcula os valores da função seno para cada ponto em x
y = np.sin(x)

# Cria o gráfico
plt.plot(x, y, label='Função Seno')
plt.title('Gráfico da Função Seno')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()
plt.grid(True)

# Exibe o gráfico
plt.show()