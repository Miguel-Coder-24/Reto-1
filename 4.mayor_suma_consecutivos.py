#* Escribir una función que reciba una lista de numeros enteros
#  y retorne la mayor suma entre dos elementos consecutivos.

def mayor_suma_consecutivos(lista):
    """Devuelve la mayor suma entre dos elementos consecutivos de una lista"""
    if len(lista) < 2:  # Deben ser al menos dos elementos
        return "ERROR" # De no ser así retorna ERROR
    mayor_suma = lista[0] + lista[1]  
    # Se inicializa con la suma de los dos primeros elementos

    for i in range(len(lista) - 1): 
    # El bucle recorre la lista hasta el penúltimo índice
        suma = lista[i] + lista[i + 1]
        if i == 0 or suma > mayor_suma:
            mayor_suma = suma
         # Actualiza la variable mayor_suma si es la primera iteración o
         # si la nueva suma es mayor que la actual
         # De esta manera se asegura el valor más alto al final
    return mayor_suma

entrada = (input("Ingrese una lista de números separados por comas: "))
lista = list(map(int, entrada.split(",")))
resultado = mayor_suma_consecutivos(lista)
print("La mayor suma entre dos elementos consecutivos es:", resultado)

# Explicación: 
# Se pide al usuario una lista de números separados por comas,
# luego calcula la mayor suma entre dos elementos consecutivos de esa 
# lista. Si la lista tiene menos de dos elementos, devuelve "ERROR". 
# Recorre la lista sumando cada par consecutivo y guarda el valor más 
# alto encontrado. Finalmente, muestra ese valor al usuario.