'''
CONVERSOR TIEMPO
Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
'''

def conversor_tiempo(días, horas, minutos, segundos):
    días_miliseg = días * 86400000
    horas_miliseg = horas * 3600000
    minutos_miliseg = minutos * 60000
    segundos_miliseg = segundos * 1000
    milisegundos = días_miliseg + horas_miliseg + minutos_miliseg + segundos_miliseg
    print (milisegundos)

conversor_tiempo(5, 43, 45, 290)