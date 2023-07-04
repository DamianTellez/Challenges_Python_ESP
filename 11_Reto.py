'''
ELIMINANDO CARACTERES
Crea una función que reciba dos cadenas como parámetro (str1, str2) 
e imprima otras dos cadenas como salida (out1, out2).
 - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
'''

def elimina_caracteres(texto_1, texto_2):
    texto_1 = list(texto_1)
    texto_2 = list(texto_2)
    
    salida_1 = ''
    salida_2 = ''
    for caracter in texto_1:
        if caracter not in texto_2:
            salida_1 += caracter
    for caracter in texto_2:
        if caracter not in texto_1:
            salida_2 += caracter

    return(salida_1, salida_2)

print(elimina_caracteres('hola como estas', 'pedo de moco'))