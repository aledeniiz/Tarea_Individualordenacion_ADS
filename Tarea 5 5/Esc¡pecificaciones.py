from typing import List

def está_explorado(t: List[int], inicio: int, fin: int) -> bool:

    k = contar_segmentos(t, inicio, fin)
    segmentos = obtener_segmentos(t, inicio, fin, k)

    for segmento in segmentos:
        maximo = max(segmento)
        indice_maximo = segmento.index(maximo)
        
        # Hacer copia de seguridad del max del segmento
        copia_maximo = t[inicio + indice_maximo]

        # Desplazar los elementos del segmento una celda hacia la izquierda
        for i in range(indice_maximo, len(segmento) - 1):
            t[inicio + i] = t[inicio + i + 1]
        
        # Colocar el elemento más grande del segmento en la posición inicial
        t[inicio + len(segmento) - 1] = copia_maximo

    return True

def contar_segmentos(t: List[int], inicio: int, fin: int) -> int:
    segmentos = 0
    i = inicio
    while i <= fin:
        if i == fin or t[i] > t[i + 1]:
            segmentos += 1
        i += 1
    return segmentos

def obtener_segmentos(t: List[int], inicio: int, fin: int, k: int) -> List[List[int]]:
    segmentos = []
    i = inicio
    while i <= fin:
        segmento = []
        while i <= fin and (not segmento or t[i] <= t[i - 1]):
            segmento.append(t[i])
            i += 1
        segmentos.append(segmento)
        i += 1
    return segmentos

t = [5, 8, 12, 18, 16, 14, 21, 9, 4, 3, 2, 1]
inicio = 5
fin = 11
if está_explorado(t, inicio, fin):
    print("El segmento está completamente explorado.")
else:
    print("El segmento no está completamente explorado.")