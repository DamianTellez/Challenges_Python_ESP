'''
EN MAYÚSCULA
Crea una función que reciba un String de cualquier tipo 
y se encargue de poner en mayúscula la primera letra de cada palabra.
- No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''
def mayus(texto):
    texto = texto.lower()
    texto_lista = list(texto)
    n_de_letras = len(texto_lista) #Numero de letras
    
    
    for letras in range(0, n_de_letras - 1):  
        if letras == 0:
            texto_lista[letras] = texto_lista[letras].upper()
        elif texto_lista[letras] == ' ':
            texto_lista[letras + 1] = texto_lista[letras + 1].upper() 
        
    for x in texto_lista:      
        print(x, end = '')
    
entrada = input('Introduce tu texto aqui\n')
mayus(entrada)