'''
ITERATION MASTER
Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
¿De cuántas maneras eres capaz de hacerlo?
Crea el código para cada una de ellas.
'''

for x in range(1, 101):
    print(x)
#####################

x = 1
while x < 101:
    print(x)
    x += 1

#####################

numeros = ''
for x in range(1, 101):
    numeros += str(x) + '\n'
print(numeros)