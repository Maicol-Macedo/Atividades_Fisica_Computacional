import numpy as np
import matplotlib.pyplot as plt

# Função que implementa o mapa logístico
def mapa_logistico(r, x0, N):
    x = [x0]  # Inicializa a lista com o valor inicial x_0
    for n in range(1, N+1):
        x_n = r * x[-1] * (1 - x[-1])  # Aplica a equação do mapa logístico
        x.append(x_n)
    return x

# Parâmetros
M = 5000  # Últimos M valores
N = M + 1000  # Número total de iterações

# Intervalo de r de 1 até 4
r_values = np.arange(1, 4.1, 0.01)
x0 = 0.1  # Condição inicial

# Plotando os gráficos
plt.figure(figsize=(10, 6))

for r in r_values:
    # Gerar os valores do mapa logístico
    xn = mapa_logistico(r, x0, N)

    # Plotar os últimos M valores
    plt.plot(r * np.ones(M), xn[-M:], 'b.', markersize=0.5)


# Configurações de aparência do gráfico
plt.xlabel("r (Parâmetro de crescimento)")
plt.ylabel("Valores de $x_n$")
plt.title("Diagrama de bifurcação do mapa logístico")
#plt.grid(True)
plt.tight_layout()

# Exibir o gráfico
plt.show(block = True)