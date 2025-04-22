 #* Escribir una función que reciba una lista de números y devuelva sólo
#* aquellos que son primos. 
#* la función debe recibir una lista de enteros y 
#* retornar solo aquellos que sean primos.

def es_primo(num):
    """Verifica si un número es primo"""
    if num < 2: #* Los números menores que 2 no son primos.
        return False 
    if num == 2: #* El número 2 es primo.
        return True
    for i in range(2, int(num**0.5) + 1):
 #* Verifica si el número es divisible por algún número entre 2
 #* y la raíz cuadrada de num. si es divisible, no es primo.
            if num % i == 0:
                return False
    return True #* Si no es divisible por ningún número, es primo.


entrada = input("Ingrese una lista de números separados por comas: ")
numeros = list(map(int,entrada.split(",")))
#* Se utiliza split para separar los números por comas.
#* Se convierte la entrada en una lista de números enteros con int.
#* Se utiliza la función map para aplicar la conversión a cada elemento de la lista.
#* Se utiliza list para convertir el resultado de map en una lista.

primos = [num for num in numeros if es_primo(num)]
# [num for num in numeros]: Itera sobre cada número en la lista numeros.
#* Se utiliza una comprensión de lista para filtrar los números primos
print("Los números primos son:", primos)
# Muestra los números primos encontrados en la lista proporcionada por el usuario.

#* Explicación: La función `es_primo` verifica si un número es primo.
#* El menor primo es 2 por ende cualquier número menor a dos lo retornará 
#* como False.
#* Busca uno por uno desde 2 hasta la raiz cuadrada del numero a verificar
#* Si encuentra uno por el que es divisible return false, si no, return 
#* True.
