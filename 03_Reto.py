'''
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar 
si un número es o no primo.
Un número primo es un número natural mayor que 1 que 
tiene únicamente dos divisores positivos distintos:
él mismo y el 1.
Hecho esto, imprime los números primos entre 1 y 100.

'''
def primo(numero):
    if numero < 2:
        return False
    for x in range (2, numero):
        if numero % x == 0:
            return False
    return True

print(primo(1))
print(primo(2))
print(primo(3))
print(primo(4))

for num in range(1, 101):
    if primo(num) == True:
        print(num)