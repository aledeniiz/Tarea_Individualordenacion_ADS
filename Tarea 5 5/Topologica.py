from collections import defaultdict, deque

def ordenacion_topologica(n, restricciones):
    # Inicializar el grafo y el grado de entrada de cada nodo
    grafo = defaultdict(list)
    grado_entrada = [0] * (n + 1)
    
    # Construir el grafo y calcular el grado de entrada de cada nodo
    for restriccion in restricciones:
        i, j = restriccion
        grafo[i].append(j)
        grado_entrada[j] += 1
    
    # Inicializar una cola para los nodos sin dependencias
    cola = deque([i for i in range(1, n + 1) if grado_entrada[i] == 0])
    
    # Inicializar el orden topológico
    orden_topologico = []
    
    # Procesar los nodos en orden topológico
    while cola:
        nodo = cola.popleft()
        orden_topologico.append(nodo)
        
        # Reducir el grado de entrada de los nodos adyacentes
        for vecino in grafo[nodo]:
            grado_entrada[vecino] -= 1
            if grado_entrada[vecino] == 0:
                cola.append(vecino)
    
    # Verificar si se cumplen todas las restricciones
    if len(orden_topologico) != n:
        return None  
    
    return orden_topologico

n = 5
restricciones = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
orden = ordenacion_topologica(n, restricciones)
if orden:
    print("Orden topológico:", orden)
else:
    print("No se puede cumplir todas las restricciones, no hay ordenación.")