# INICIANDO PRUEBA
# Creamos un nuevo archivo llamado my_notes.txt en modo de escritura
with open("my_notes.txt", "w") as file:
    # Escribimos algunas notas personales en el archivo
    file.write("Estas son mis notas personales:\n")
    file.write("- Pasar el ciclo sin dificultades.\n")
    file.write("- Encomendarse a Diosito.\n")
    file.write("- Ir a misa por viernes santo.\n")

# Abrimos el archivo en modo de lectura
with open("my_notes.txt", "r") as file:
    # Leemos el contenido del archivo línea por línea
    for line in file.readlines():
        # Mostramos cada línea leída en la consola
        print(line.strip())  # Utilizamos strip() para eliminar los caracteres de nueva línea