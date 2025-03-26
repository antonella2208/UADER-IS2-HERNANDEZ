import matplotlib.pyplot as plt

def collatz_iterations(n):
    """Calcula el número de iteraciones necesarias para que la secuencia de Collatz llegue a 1."""
    count = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    return count

x_values = list(range(1, 10001))
y_values = [collatz_iterations(n) for n in x_values]

plt.figure(figsize=(10, 6))
plt.scatter(y_values, x_values, s=1, color='blue', alpha=0.5)
plt.xlabel("Número de Iteraciones")
plt.ylabel("Número Inicial (n)")
plt.title("Número de Iteraciones en la Conjetura de Collatz (1-10,000)")
plt.grid(True, linestyle="--", alpha=0.5)

plt.savefig("collatz_graph.png", dpi=300)
plt.show()
