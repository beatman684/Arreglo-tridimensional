def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def ordenar_fila_matriz(matriz, fila):
    fila_a_ordenar = matriz[fila]
    bubble_sort(fila_a_ordenar)
    matriz[fila] = fila_a_ordenar

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Matriz original
matriz_original = [
    [9, 2, 5],
    [7, 1, 8],
    [3, 6, 4]
]

print("Matriz Original:")
mostrar_matriz(matriz_original)


fila_a_ordenar = 1
ordenar_fila_matriz(matriz_original, fila_a_ordenar)

print("\nMatriz con la fila", fila_a_ordenar + 1, "ordenada:")
mostrar_matriz(matriz_original)

