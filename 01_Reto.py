'''
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
 '''

def anagrama(palabra_1, palabra_2): #Definimos una funcion con dos strings
    palabra_1 = palabra_1.lower() #Nos aseguramos que no hayan errores con las mayus haciendo ambos strings minuculas
    palabra_2 = palabra_2.lower()
    lista_palabra_1 = list(palabra_1) #Pasamos los strings a listas para tener en cuenta cada letra de la palabra
    lista_palabra_2 = list(palabra_2)
    lista_palabra_1.sort() #Ordenamos las letras de ambas palabras
    lista_palabra_2.sort()
    if palabra_1 == palabra_2:
        print(False, 'Es la misma palabra') 
    elif len(lista_palabra_1) != len(lista_palabra_2):
        print(False, 'Ni siquiera tienen el mismo número de letras') #Directamente si no tienen el mismo numero de letras imprime False
    elif lista_palabra_2 == lista_palabra_1:
        print(True, 'Es un anagrama')
    else:
        print(False, 'No es un anagrama')

anagrama('hola','hola')
anagrama('hola', 'holi')
anagrama('hola', 'ola')
anagrama('hola', 'Aloh')