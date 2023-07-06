'''
FACTORIAL RECURSIVO
Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
numero factorial :
n! = n * (n-1) * (n-1) - 1 * .... * 1
ej:
3 = 3 * 2 * 1
'''
def factorial_recursivo(n):
    anterior = n - 1
    if n == 0:
        print ('0')
    elif n == 1:
        print('1')
    else:
        for x in range(2, n + 1): 
            n_recursivo = n * anterior
            anterior = anterior - 1
            n = n_recursivo
        print(n_recursivo)

Entrada = input('Escribe el numero que quieres calcular\n')
factorial_recursivo(int(Entrada))

