# Función que encuentra la palabra con más caracteres (y ordenada alfabéticamente en caso de empate)
def mas_caracteres(lista_palabras):
    return max(lista_palabras, key=lambda palabra: (len(palabra), palabra))

# Lista de ejemplo
palabras = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con más caracteres:", mas_caracteres(palabras))
