'''
VECTORES ORTOGONALES
Crea un programa que determine si dos vectores son ortogonales.
 - Los dos array deben tener la misma longitud.
 - Cada vector se podría representar como un array. Ejemplo: [1, -2]
'''
def ortogonales(vector_1, vector_2):
    if vector_1[0]*vector_2[0] + vector_1[1]*vector_2[1] == 0:
        return True
    else:
        return False
    
print(ortogonales([1,-2], [2, 1]))
