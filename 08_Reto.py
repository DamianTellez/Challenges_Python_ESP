'''
DECIMAL A BINARIO
Crea un programa se encargue de transformar un número decimal a binario 
sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''

def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    
    binario = ''
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    
    return binario
    
print(decimal_a_binario(10))