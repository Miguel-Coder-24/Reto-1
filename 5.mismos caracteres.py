#Escribe una función que reciba una lista de string y retorne unicamente 
# aquellos elementos que tengan los mismos caracteres.


def mismos_caracteres(lista):
    resultado = []
    for palabra in lista:
        for otra_palabra in lista:
            if set(palabra) == set(otra_palabra) and palabra != otra_palabra:
                resultado.append(palabra)
                break  # Salimos del ciclo interno si ya encontramos un par
    return list(set(resultado))  
    # Eliminamos duplicados en el resultado antes de retornarlo


lista = input("Ingrese una lista de palabras separadas por comas: ").split(",")


resultado = mismos_caracteres(lista)
print("Las palabras que tienen exactamente los mismos caracteres en común son:", resultado)

#* Explicación:
# Primero, el programa pide al usuario una lista de palabras separadas
# por comas y las convierte en una lista. Luego, la función recorre cada
#  palabra y la compara con todas las demás. Si encuentra otra palabra 
# que tenga exactamente los mismos caracteres, guarda la palabra en una
# lista de resultado. Para evitar repeticiones, al final 
# elimina duplicados antes de mostrar las coincidencias.