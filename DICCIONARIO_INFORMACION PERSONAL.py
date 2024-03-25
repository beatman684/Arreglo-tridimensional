# INICIANDO PRUEBA
# Diccionario informacion_personal
informacion_personal = {
    "nombre": "Andres",
    "edad": 30,
    "ciudad": "Loja",
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Cuenca"

# Agregar una nueva clave-valor
informacion_personal["profesion"] = "Diseñador Grafico"

# Verificar si la clave "teléfono" existe
if "teléfono" not in informacion_personal:
    # Si no existe, agregarla con un número de teléfono ficticio
    informacion_personal["teléfono"] = "09999484849384"

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# Imprimir diccionario actualizado
print(informacion_personal)