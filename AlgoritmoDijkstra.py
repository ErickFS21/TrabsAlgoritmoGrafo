import heapq
#--------------
#Função DIJKSTRA
#--------------
def dijkstra(grafo, inicio):
    distancias = {vertice: float('inf')for vertice in grafo}
    distancias[inicio]=0
    fila = [(0,inicio)]
    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)
        for vizinho, peso in grafo[vertice_atual]:
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(fila,(nova_distancia, vizinho))
    return distancias

#-----------------
#Entrada do grafo
#-----------------
grafo = {}
qtd_vertices = int(input("Quantidade de vértices:"))
# Criando Vértices
for i in range(qtd_vertices):
    vertice = input(f"Nome do vértice {i+1}:")
    grafo[vertice]=[]

qtd_arestas = int(input("Quantidade de arestas:"))
#Inserindo arestas
for i in range(qtd_arestas):
    origem = input("Origem:")
    destino = input("Destino:")
    peso = int(input("Peso de aresta:"))
    #Grafo não direcionado
    grafo[origem].append((destino, peso))
    grafo[destino].append((origem, peso))
#--------
#Execução
#--------
inicio = input("Vértice inicial:")
resultado = dijkstra(grafo, inicio)
print("\nMenores distâncias:")
for vertice, distancia in resultado.items():
    print(f"{inicio}->{vertice} = {distancia}")