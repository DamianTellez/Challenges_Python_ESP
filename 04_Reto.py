'''
ÁREA DE UN POLÍGONO
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
La función recibirá por parámetro sólo UN polígono a la vez.
Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
Imprime el cálculo del área de un polígono de cada tipo.
'''

#Primero definimos las 3 clases distintas de poligonos

class Triángulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

class Rectángulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

#Creamos 3 poligonos distintos para hacer la prueba

triangulo_1 = Triángulo(3, 3)
cuadrado_1 = Cuadrado(2)
rectangulo_1 = Rectángulo(1, 3)

#Creamos la función

def area(poligono):
    if isinstance(poligono, Triángulo): #Si 'poligono' está dentro de 'Triangulo' entonces:
        print (poligono.base * poligono.altura / 2)
    elif isinstance(poligono, Cuadrado):
        print (poligono.lado ** 2)
    elif isinstance(poligono, Rectángulo):
        print (poligono.base * poligono.altura)

#Probamos las áreas de los poligonos ya creados

area(triangulo_1)
area(cuadrado_1)
area(rectangulo_1)