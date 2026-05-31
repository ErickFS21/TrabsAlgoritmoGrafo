#=========================================
#ALGORITMO DE PRIM - GRAFO NÃO DIRECIONADO
#COM TRATAMENTO DE ERROS
#VÉRTICES COMEÇANDO EM 1
#=========================================
import heapq
#=========================================
#função do algoritmo de prim
#=========================================
def prim(grafo, inicio):
    visitados = set()
    fila_prioridade = []
    visitados.add(inicio)
    # Adiciona as arestas do vertice inicial
    for vizinho, peso in grafo[inicio]:
        heapq.heappush(fila_prioridade, (peso, inicio, vizinho))
    arvore_minima= []
    custo_total= 0
    while fila_prioridade:
        peso, origem, destino = heapq.heappop(fila_prioridade)
        if destino not in visitados:
            visitados.add(destino)
            arvore_minima.append((origem,destino,peso))
            custo_total += peso
            for vizinho, peso_aresta in grafo[destino]:
                if vizinho not in visitados:
                    heapq.heappush(
                        fila_prioridade,
                        (peso_aresta,destino,vizinho)
                        )
    return arvore_minima, custo_total
#=====================================
#PROGRAMA PRINCIPAL
#=====================================
print("="*60)
print("ALGORITMO DE PRIM - GRAFO NÃO DIRECIONADO")
print("="*60)
#=====================================
#LEITURA DO NÚMERO DE VÉRTICES
#=====================================
while True:
    try:
        num_vertices= int(input("Digite o número de vértices:"))
        if num_vertices<= 0:
            print("ERRO: O número de vértices deve ser maior que zero.\n")
        else:
            break
    except ValueError:
         print("ERRO: Digite apenas números inteiros.\n")
#====================================
#LEITURA DO NÚMERO DE ARESTAS
#====================================
while True:
    try:
        num_arestas = int(input("Digite o número de arestas: "))
        if num_arestas<=0:
            print("ERRO:O número de arestas deve ser maior que zero.\n")
        else:
            break
    except ValueError:
            print("ERRO: digite apenas números inteiros.\n")
#------------------
#criação do grafo
#------------------
grafo = {}
for i in range(1,num_vertices + 1):
    grafo[i] = []
print("\nDigite as arestas no formato:")
print("origem destino peso")
print("exemplo: 1 2 10\n")
#-------------------
#leitura das arestas
#-------------------
for i in range(num_arestas):
    print(f"\nAresta {i+1}")
    while True:
        try:
            origem = int(input("Origem: "))
            destino = int(input("Destino: "))
            #verifica se os vértices existem
            if origem not in grafo:
                print(f"ERRO: O vértice {origem} não existe")
                print(f"Os vértices válidos vão de 1 até {num_vertices}.\n")
                continue
            if destino not in grafo:
                print(f"ERRO: o vertice {destino} não existe.")
                print(f"os vertices validos vão de 1 até {num_vertices}.\n")
                continue
            peso = float(input("peso: "))
            #adiciona aresta no grafo
            grafo[origem].append((destino, peso))
            grafo[destino].append((origem, peso))
            break
        except ValueError:
            print("ERRO: entrada invalida. Digite numeros corretamente\n")
#---------------------
#execução do algoritmo
#---------------------
vertice_inicial = 1
agm, custo_total = prim(grafo,vertice_inicial)
#---------------------
#resultados
#---------------------
print("\n" + "=" * 60)
print("ARVORE GERADORA MINIMA(PRIM)")
print("=" * 60)
for origem, destino, peso in agm:
    print(f"{origem}---{destino}|peso = {peso}")
print("=" * 60)
print(f"custo total da AGM: {custo_total}")
      