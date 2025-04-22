# 1. Crear una función que realice operaciones básicas (suma, resta,
# multiplicación, división) entre dos números, según la elección del
# usuario, la forma de entrada de la función será los dos operandos y 
# el caracter usado para la operación. Entrada: (1,2,"+"), salida (3).


def funcion_aritmetica(num1, num2, operador): 
    """Realiza operaciones básicas entre dos números"""
# Definimos la función con 3 parámetros; dos números y un operador.
# Los operadores serán:
    if operador == "+": # Suma "+"
        return num1 + num2
    elif operador == "-": # Resta "-"
        return num1 - num2
    elif operador == "*": # Multiplicación "*"
        return num1 * num2
    elif operador == "/": # División "/"
        if num2 != 0: # Verificamos que el segundo número no sea cero,
# así evitamos la división por cero
            return num1 / num2
        else:
            return "Error: división por cero" 
# Si el segundo número es cero, devolvemos un mensaje de error
    else:     
        return "operador no valido" 
# Si el operador no es válido, devolvemos un mensaje de error
    

print("Bienvenido a la calculadora")
print("Operaciones disponibles: +, -, *, /")
entrada = input("Ingrese los dos números y el operador separados por comas "
"(ejemplo: 5,3,+): ")
num1, num2, operador = entrada.split(",")  
# Divide la entrada en tres partes, usa la coma como delimitador
num1 = int(num1)  # Convierte el primer número a entero
num2 = int(num2)  # Convierte el segundo número a entero
resultado = funcion_aritmetica(num1, num2, operador)  
# Llama a la función
print("El resultado de la operación es:", resultado)


# Explicación: La función `funcion_aritmetica` 
# implementa una calculadora básica con las operaciones: 
# suma, resta, multiplicación y división entre dos números.
# Toma dos números y un operador como entrada. Dependiendo del operador,
# realiza la operación correspondiente y devuelve el resultado. (para 
# la división retorna un mensaje de error si el segundo número es 0.
# Si el operador no es válido, devuelve un mensaje de error.