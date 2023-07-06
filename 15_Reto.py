'''
¿CUÁNTOS DÍAS?
Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 - La función recibirá dos String y retornará un Int.
 - La diferencia en días será absoluta (no importa el orden de las fechas).
 - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
'''

from datetime import date

def dias(fecha_1, fecha_2):
    try:
        fecha_1 = fecha_1.split('/')
        fecha_1 = [int(x) for x in fecha_1] 
        fecha_1 = date(fecha_1[2], fecha_1[1], fecha_1[0])
        fecha_2 = fecha_2.split('/')
        fecha_2 = [int(x) for x in fecha_2] 
        fecha_2 = date(fecha_2[2], fecha_2[1], fecha_2[0])
    
        if fecha_1 > fecha_2:
            dias_de_diferencia = fecha_1 - fecha_2
            print(dias_de_diferencia)
        elif fecha_2 > fecha_1:
            dias_de_diferencia = fecha_2 - fecha_1
            print(dias_de_diferencia)
    except:
        print('Debes introducir la fecha en un formato soportable')

entrada = input('Introduce la primera fecha con este formato dd/mm/yyyy\n')
entrada_2 = input('Introduce la segunda fecha con este formato dd/mm/yyyy\n')
dias(entrada, entrada_2)
