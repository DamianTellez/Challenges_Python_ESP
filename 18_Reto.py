'''
TRES EN RAYA
Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
- "X" si han ganado las "X"
- "O" si han ganado los "O"
- "Empate" si ha habido un empate
- "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.  O si han ganado los 2.
Nota: La matriz puede no estar totalmente cubierta.
Se podría representar con un vacío "", por ejemplo.
'''

def tres_en_raya(matriz):
    resultado = ''
    for x in range(2):
        if matriz[x][0] == matriz[x][1] == matriz[x][2]:
            resultado += matriz[x][0]
        elif matriz[0][x] == matriz[1][x] == matriz[2][x]:
            resultado += matriz[0][x]
        elif matriz[0][0] == matriz [1][1] == matriz[2][2]:
            resultado += matriz[0][0]
        elif matriz[0][2] == matriz [1][1] == matriz [2][0]:
            resultado += matriz [0][2]
    count_x = 0
    count_O = 0
    for lista in matriz:
        for elementos in lista:
            if elementos == 'X':
                count_x += 1
        for elementos in lista:
            if elementos == 'O':
                count_O += 1

    resultado_lista = list(resultado)
   
    if resultado == '' or count_x + 2 == count_O or count_x == count_O + 2 or count_x + 3 == count_O or count_x + 4 == count_O or count_x + 5 == count_O or count_x == count_O + 3 or count_x == count_O + 4 or count_x == count_O + 5 or count_x + 6 == count_O or count_x == count_O + 6 or count_x + 7 == count_O or count_x == count_O + 7 or count_x + 8 == count_O or count_x + 9 == count_O or count_x == count_O + 8 or count_x == count_O + 9:
        print('Nulo')    
    elif len(resultado_lista) > 1:
        print('Empate')  
    else:
        print(resultado)
    


matriz = [['X', 'O', 'X'],
          ['X', 'O', 'O'],
          ['X', '', '']]

tres_en_raya(matriz)

matriz_1 = [['X', 'O', 'X'],
          ['', 'O', 'O'],
          ['X', '', '']]

tres_en_raya(matriz_1)

matriz_2 = [['X', 'O', 'X'],
          ['X', 'O', 'O'],
          ['X', 'O', 'O']]

tres_en_raya(matriz_2)

matriz_3 = [['X', 'O', 'O'],
          ['X', 'O', 'O'],
          ['X', 'O', 'O']]

tres_en_raya(matriz_3)