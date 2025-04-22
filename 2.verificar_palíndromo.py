
#Realice una función que permita validar si una palabra es un palíndromo.
#Condición: No se vale hacer Slicing para invertir la palabra y verificar
#que sea igual a la original.

def es_palindromo(palabra):
    """Verifica si una palabra es un palíndromo"""
    palabra = palabra.replace(" ", "").lower()
#* Elimina los espacios y se convierten todas las letras a minúsculas.
    palabra_invertida = ""
#* Se inicializa una variable vacía para almacenar la palabra invertida.
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida
#* Se recorre la palabra original letra por letra,
#  agregando cada letra al inicio de la variable `palabra_invertida`.
#* Esto invierte el orden de las letras.
    return palabra == palabra_invertida
#* Se compara la palabra original con la invertida.
#* Si son iguales, se devuelve `True`, indicando que es un palíndromo.
#* Si no son iguales, se devuelve `False`, indicando que no es un palíndromo.   

palabra = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra):    
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")  


#* Explicación: La función `es_palindromo` verifica si una palabra 
#* o frase es un palíndromo. Primero se eliminan los espacios y se reduce
#* todo a minusculas, se crea una variable llamada palabra_invertida, 
#* inicialmente vacia donde se almacenará la palabra invertida,
#* se recorre la palabra original letra por letra hasta invertir 
#* completamente la palabra y se compara si la palabra original es igual
#* a la invertida retorna True y se muestra "es un palíndromo" o False 
#* y se muestra "no es un palíndromo."