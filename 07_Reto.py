'''
CONTANDO PALABRAS
Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''
texto = 'Me llamo Maria. Me gustan las mascotas, en especial los perros. Tengo 8 perros. En mi casa hay 2 mascotas, 1 de ellas es un perro'

import re

def len_palabras(palabra):
    print(len((re.findall(palabra, texto, re.I))))

len_palabras('perroS')

'''
Otra manera
'''
import re
texto_enminus = texto.lower() #Pasamos el texto a minusculas entero
texto_lista_sin_puntuacion = re.sub(r'[^\w\s]', ' ', texto_enminus) #cambiamos los signos de puntuacion por espacios en blanco
texto_lista = texto_lista_sin_puntuacion.split() #Dividimos las palabras en la lista con .split

def len_palabras_2 (palabra): 
    print(texto_lista.count(palabra.lower())) #Convertimos la palabra que vayamos a buscar en minusculas y hacemos un count para contar

len_palabras_2('pERrOs')

