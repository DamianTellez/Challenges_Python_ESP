'''
PIEDRA, PAPEL, TIJERA
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
- El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
- La función recibe un listado que contiene pares, representando cada jugada.
- El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
- Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
'''

def ppt(matriz):
    player_1 = ''
    player_2 = ''
    for x in range(0, len(matriz)):
        if matriz[x][0] == 'R' and matriz[x][1] == 'S':
            player_1 += 'W'
        elif matriz[x][0] == 'S' and matriz[x][1] == 'R':
            player_2 += 'W'
        elif matriz[x][0] == 'R' and matriz[x][1] == 'P':
            player_2 += 'W'
        elif matriz[x][0] == 'P' and matriz[x][1] == 'R':
            player_1 += 'W'
        elif matriz[x][0] == 'P' and matriz[x][1] == 'S':
            player_2 += 'W'
        elif matriz[x][0] == 'S' and matriz[x][1] == 'P':
            player_1 += 'W'
    
    numero_de_ganadas_1 = len(list(player_1))
    numero_de_ganadas_2 = len(list(player_2))

    if numero_de_ganadas_1 > numero_de_ganadas_2:
        print('Player 1 WIN')
    elif numero_de_ganadas_2 > numero_de_ganadas_1:
        print('Player 2 WIN')
    else:
        print('Tie')

matriz_jugadas = [("R","S"),
                ("S","R"), 
                ("P","S")]

ppt(matriz_jugadas)