import time
import sys
from binarytree import Node


def rod_cut(nodo, total, arreglo, n, cont, mayor):
	"""Función para calcular el máximo ganancias (en dinero) 
	dependiendo del tamaño de la varilla y si se corta o no """
	
	if n == len(arreglo):
		# Cuando lleva al último nivel, guardamos los cortes de 
        # las varillas con su precio máximo en el nodo hoja
		total += arreglo[cont - 1]
		nodo.value = total
		if mayor[0] < total:
			# Guardamos en la lista el número de la ganancia máxima
			mayor[0] = total
	else:
		# Si no es el último nivel, creamos los dos nodos izq y derecha, 
        # y vamos expandiendo el árbol por izq y der
		nodo.left = Node(0)
		nodo.right = Node(0)
		n += 1  # Contador para los niveles del árbol (k = 1, k = 2, etc)
		rot_cut_izq(nodo.left, total, arreglo, n, cont, mayor)
		rot_cut_der(nodo.right, total, arreglo, n, cont, mayor)


def rot_cut_izq(nodo, total, arreglo, n, cont, mayor):
    """Función para ir expandiendo el árbol por la izquierda"""
	
    cont += 1  #Guarda el tamaño de la varilla sin cortar
    rod_cut(nodo, total, arreglo, n, cont, mayor)


def rot_cut_der(nodo, total, arreglo, n, cont, mayor):
    """Función para ir expandiendo el árbol por la derecha"""
	
    total += arreglo[cont - 1]  # Cada vez que se corta, vamos sumando el precio máximo de la longitud de la varilla
    cont = 1  # Se reinicia el contador cuando se corta la varilla
    rod_cut(nodo, total, arreglo, n, cont, mayor)


root = Node(0)  # Creamos el nodo raiz
root.left = None
root.right = None
arreglo = [1, 5, 8, 9, 10, 13] 
n = 1
cont = 1
total = 0
mayor = [-sys.maxsize - 1]  # Menor valor de un entero en python

inicio = time.time()
rod_cut(root, total, arreglo, n, cont, mayor)
fin = time.time()

print(root)  #Imprime el árbol en forma gráfica

print("Mayor", mayor[0])
print("Tiempo en segundos - Backtracking: ", fin - inicio)