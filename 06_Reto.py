'''
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 '''


def invertir(texto):
    texto_invertido = ''
    numero_letras = len(texto)
    for letras in range(numero_letras-1, -1, -1):
        texto_invertido += texto[letras]
    return texto_invertido

print(invertir('Hola mundo'))
