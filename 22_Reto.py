'''
CONJUNTOS
Crea una función que reciba dos array, un booleano y retorne un array.
- Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
- Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''
def conjuntos(array_1, array_2, booleano):
    if booleano == True:
        array_3 = ''
        for x in range(0, len(array_1)) :
            if array_1[x] in array_2 :
                array_3 += array_1[x] + ' '
        return array_3
    if booleano == False:
        array_3 = ''
        for x in range(0, len(array_1)) :
            if array_1[x] not in array_2 :
                array_3 += array_1[x] + ' '
        return array_3

lista_1 = ['Loro','Leon','Lado','Libelula','Lirio']
lista_2 = ['La','Libelula','Posada','En', 'El', 'Lirio']
print(conjuntos(lista_1, lista_2, True))
print(conjuntos(lista_1, lista_2, False))