import heapq
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
def dijkstra(grafo,inicio):
    distancias = {vertice: float("infinity") for vertice in grafo}
    distancias[inicio]=0
    
    fila_prioridade = [(0,inicio)]
    
    while fila_prioridade:
        dist_atual, vertice_atual =heapq.heappop(fila_prioridade)
        
        if dist_atual > distancias[vertice_atual]:
            continue        
        
        for vizinho, peso in grafo[vertice_atual]:
            distancia = dist_atual + peso
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia,vizinho))
                
    return distancias


resultado = dijkstra(grafo, 'A')
print(resultado)