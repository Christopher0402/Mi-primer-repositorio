#Programa que calcula la raiz cuadrada de un numero
import math

# Pedir número al usuario que ingrese un numero
numero = float(input("Ingresa un número: "))

# Verificar si el número es negativo
if numero < 0:
    print("No se puede calcular la raíz cuadrada de un número negativo.")
else:
    resultado = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es: {resultado}")
