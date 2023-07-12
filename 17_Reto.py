'''
LA CARRERA DE OBSTÁCULOS
Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
- La función recibirá dos parámetros:
- Un array que sólo puede contener String con las palabras "run" o "jump"
- Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
- La función imprimirá cómo ha finalizado la carrera:
- Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto 
y no variará el símbolo de esa parte de la pista.
- Si hace "jump" en "_" (suelo), se variará la pista por "x".
- Si hace "run" en "|" (valla), se variará la pista por "/".
- La función retornará un Boolean que indique si ha superado la carrera.
Para ello tiene que realizar la opción correcta en cada tramo de la pista.
'''

def carrera(acciones, pista):
    elementos_pista = list(pista)
    pista_final = ''
    for x in range(0, len(elementos_pista)):
        if acciones[x] == 'run' and elementos_pista[x] == '_':
            pista_final += elementos_pista[x]
        elif acciones[x] == 'run' and elementos_pista[x] == '|':
            pista_final += '/'
        elif acciones[x] == 'jump' and elementos_pista[x] == '_':
            pista_final += 'x'
        elif acciones[x] == 'jump' and elementos_pista[x] == '|':
            pista_final += elementos_pista[x]
        else:
            print('Las acciones o la pista introducida no son válidas')
    
    print(pista_final)

    if pista == pista_final:
        return True
    else:
        return False
    

print(carrera(['run','jump','jump','jump', 'jump'], '__|_|'))
print(carrera(['run','run','jump','run', 'jump'], '__|_|'))
print(carrera(['run','run','jump','jump', 'run'], '__|_|'))
print(carrera(['jump','jump','jump','run', 'jump'], '__|_|'))
print(carrera(['run','run','run','run', 'jump'], '__|_|'))
