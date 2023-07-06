'''
¿ES UN PALÍNDROMO?
Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.
'''

def palindromo(expresion):
    expresion = expresion.replace(' ', '')
    expresion = expresion.lower()
    numero_caracteres = len(expresion)
    expresion_alreves = ''
    for caracter in range(numero_caracteres -1, -1, -1):
        expresion_alreves += expresion[caracter]
    if expresion_alreves == expresion:
        return True
    else:
        return False
    
Entrada = input('Escribe tu expresión\n')
print(palindromo(Entrada))

