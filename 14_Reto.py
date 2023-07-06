'''
¿ES UN NÚMERO DE ARMSTRONG?
Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información al respecto.

numero amstrong :
n de 3 cifras = abc = (a , b , c) = a**3 + b**3 + c**3
'''

def amstrong (n):
    n_str = str(n) #Pasamos el numero a str para poder dividir cada numero de la cifra en una lista
    n_list = list(n_str) 
    cifras = len(n_list)
    n_list = [int(x) for x in n_list] #pasamos los numeros de la lista de str a int
    n_amstrong = 0 #Aqui se iran sumando los elementos del bucle siguiente
    for x in range(0, cifras):
        n_amstrong += n_list[x] ** cifras
    if n_amstrong == n:
        print('Es un numero amstrong')
    else:
        print('No es un numero amstrong')

entrada = input('Escribe el numero que quieres comprobar\n')
amstrong(entrada)
