matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
def buscar_valor(matriz, valor):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == valor:
                return f"Valor encontrado en la posicion ({i}, {j})"

    return "Valor no encontrado"


valor_a_buscar = 6

resultado = buscar_valor(matriz, valor_a_buscar)

print(resultado)