import time


def rod_cutting_problem(precios, n):
    tabla = [0 for i in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            tabla[i] = max(tabla[i], precios[j - 1] + tabla[i - j])
    print(tabla)
    return tabla[n]


precios = [1, 5, 8, 9, 10, 13, 15, 19]
n = 8
inicio = time.time()
precioMax = rod_cutting_problem(precios, n)
fin = time.time()


print(f"La ganancia es {precioMax}")
print("Tiempo en segundos: ", fin - inicio)
