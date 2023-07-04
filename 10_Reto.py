'''
EXPRESIONES EQUILIBRADAS
Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ) ] - 5 }
#Debemos hacer que encuentre en la cadena si hay ([{}]) en primer lugar,
luego si por cada ([{, haya otro }]). Es decir deben ser pares. 
Ademas, que por cada {[( tenga su correspondiente }]), mirando para el mismo lado. 
Y ademas, que si el orden es paréntesis, llave y corchete, no cambie.#

'''
dict_simbolos = {
    '(': ')',
    '{': '}',
    '[': ']',
}

def equilibrio(expresion):
    
    almacenamiento = ''
    for caracter in expresion:
        if caracter in dict_simbolos:
            almacenamiento += caracter
        elif caracter in dict_simbolos.values():
            almacenamiento += caracter

    for clave, valor in dict_simbolos.items():
        almacenamiento = almacenamiento.replace(clave + valor, '') #Hemos remplazado cada clave + su valor por ''

    if len(almacenamiento) == 0:
        return('Expresión balanceada')
    else:
        return('Expresión no balanceada')
    

Entrada = input('Escribe tu expresión\n')
print(equilibrio(Entrada))
