'''
MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''
def MCD(numero_1, numero_2):
    lista_comunes = []
    if numero_1 < numero_2:
        for x in range(1, numero_2):
            if numero_2 % x == 0 and numero_1 % x == 0:
                lista_comunes.append(x)
            
    elif numero_2 < numero_1:
        for x in range(1, numero_1):
            if numero_2 % x == 0 and numero_1 % x == 0:
                lista_comunes.append(x)
    a = len(lista_comunes)
    return (lista_comunes[a - 1])

print(MCD(765,55))
print(MCD(234,39))
print(MCD(75,360))

def mcm(numero_1, numero_2):
    lista = []
    for x in range(1, 1000):
        if x % numero_1 == 0 and x % numero_2 == 0:
            lista.append(x)
    return (lista[0])

print(mcm(3,5))
print(mcm(2,10))
print(mcm(7,3))
