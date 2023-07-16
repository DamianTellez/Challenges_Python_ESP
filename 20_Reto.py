'''
PARANDO EL TIEMPO
Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
- Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
- Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal.
Se podría ejecutar varias veces al mismo tiempo.
'''
import time
def suma_tiempo(numero_1, numero_2, tiempo):
    time.sleep(tiempo)
    suma = numero_1 + numero_2
    return suma

print(suma_tiempo(3, 4, 4))
print(suma_tiempo(6, 4, 7))
print(suma_tiempo(1, 4, 2))