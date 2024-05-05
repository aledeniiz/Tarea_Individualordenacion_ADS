def insertion_sort(t):
    """
    Ordena la lista t en su lugar utilizando el algoritmo de inserción sin tabla adicional.
    """
    for i in range(1, len(t)):
        temp = t[i]
        j = i - 1
        while j >= 0 and t[j] > temp:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = temp

# Ejemplo de uso:
t = [5, 2, 8, 1, 9, 3]
print("Lista original:", t)
insertion_sort(t)
print("Lista ordenada:", t)