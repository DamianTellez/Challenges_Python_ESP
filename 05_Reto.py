'''ASPECT RATIO DE UNA IMAGEN
Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
- Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
 '''

import requests #Este modulo se usa para acceder a url
from PIL import Image #Para uso de imagenes
import io #Para uso de bytes (contenido binario) 

#Solicitamos un get a la url
respuesta = requests.get('https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png')
#Para poder acceder al contenido de una imagen tenemos que acceder al contenido de forma binaria
imagen = respuesta.content # .text si fuera una archivo de texto, .content para imagenes
#Abrimos la imagen
imagen = Image.open(io.BytesIO(imagen)) #io.BytesIO para leer datos binarios
print(imagen) #Aqui sabemos que el size=2560x820
#Obtenemos las dimensiones y calculamos aspect ratio en decimales
ancho, altura = imagen.size
aspect_ratio = ancho / altura #El resultado es decimal es 3.1219512195121952
#Buscamos el resultado en fraccion

numerador = ancho
denominador = altura
import math
mcd = math.gcd(numerador, denominador) #Buscamos el maximo comun divisor
print(int(numerador / mcd), ':', int(denominador / mcd)) #Imprimimos el alto/mcd y el ancho/mcd