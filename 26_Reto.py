'''
CUADRADO Y TRIÁNGULO 2D
Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
- Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
- EXTRA: ¿Eres capaz de dibujar más figuras?
'''
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
class Triángulo:
    def __init__(self,lado):
        self.lado = lado

def asteriscos(lado, figura):
    asterisco = ''
    if figura == Cuadrado:
        asterisco += '* ' * lado + '\n' + ('* ' + '  ' * (lado - 2) + '* '+ '\n')* (lado - 2)+ '* ' * lado
    elif figura == Triángulo:
        for i in range(1, lado + 1):
            asterisco += '* ' * i + '\n'
    print(asterisco)

asteriscos(10, Cuadrado)
asteriscos(5, Triángulo)