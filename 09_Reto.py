'''
CÓDIGO MORSE
Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos 
y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
'''

dict_1 = {
    'a' : '._',
    'b' : '_...',
    'c' : '_._.',
    'd' : '_..',
    'e' : '.',
    'f' : '.._.',
    'g' : '__.',
    'h' : '....',
    'i' : '..',
    'j' : '.___',
    'k' : '_._',
    'l' : '._..',
    'm' : '__',
    'n' : '_.',
    'ñ' : '__.__',
    'o' : '___',
    'p' : '.__.',
    'q' : '__._',
    'r' : '._.',
    's' : '...',
    't' : '_',
    'u' : '.._',
    'v' : '..._',
    'w' : '.__',
    'x' : '_.._',
    'y' : '_.__',
    'z' : '__..',
    '0' : '_____',
    '1' : '.____',
    '2' : '..___',
    '3' : '...__',
    '4' : '..._',
    '5' : '.....',
    '6' : '_....',
    '7' : '__...',
    '8' : '___..',
    '9' : '____.',
    '.' : '._._._',
    ',' : '__..__',
    '?' : '..__..',
    '"' : '._.._.',
    '/' : '_.._.',
    }



def traductor_a_morse(texto_natural_a_morse):
    texto_natural_a_morse = texto_natural_a_morse.lower()
    texto_natural_a_morse = list(texto_natural_a_morse)
    traduccion = ''
    for letra in texto_natural_a_morse:
        if letra == ' ':
            traduccion += ' '
        elif letra in dict_1:
            traduccion += dict_1[letra] + ' '

    return traduccion

def traductor_a_natural(texto_morse):
    palabras_morse = texto_morse.split(' ') #Cada palabra en morse
    traduccion = ''
    for letras in palabras_morse:
        if letras in dict_1.values():
            for letra_traducida, morse in dict_1.items():
                if morse == letras:
                    traduccion += letra_traducida 
        else:
            traduccion += ' '
    return traduccion

import re
def  morse_a_natura_viceversa(texto):
    if re.match(r'^[A-Za-z0-9\s]+$', texto):
        return(traductor_a_morse(texto))
    elif re.match(r'^[\.\s_]+$', texto):
        return(traductor_a_natural(texto))
    else:
        return('Texto no valido')


Entrada = input('Escribe el texto a traducir\n')
print(morse_a_natura_viceversa(Entrada))