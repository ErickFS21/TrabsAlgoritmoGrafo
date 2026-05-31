#include <stdio.h>
#include <stdlib.h>

#define MAX 100

// Nó da lista de adjacência
typedef struct No {
    int numVertices;
    struct No* prox;
} No;

// Estrutura do grafo
typedef struct {
    int numVertices;
    No* listaAdj[MAX];
} Grafo;

// Criar grafo
Grafo* criarGrafo(int vertices) {
    Grafo* g = (Grafo*) malloc(sizeof(Grafo));

    if (g == NULL) {
        printf("Erro de memoria\n");
        exit(1);
    }

    g->numVertices = vertices;

    for (int i = 0; i < vertices; i++) {
        g->listaAdj[i] = NULL;
    }

    return g;
}

// Criar novo nó
No* criarNo(int v) {
    No* novo = (No*) malloc(sizeof(No));

    if (novo == NULL) {
        printf("Erro de memoria\n");
        exit(1);
    }

    novo->numVertices = v;
    novo->prox = NULL;

    return novo;
}

// Adicionar aresta (grafo orientado)
void adicionarAresta(Grafo* g, int v1, int v2) {
    if (v1 >= g->numVertices || v2 >= g->numVertices ||
        v1 < 0 || v2 < 0) {
        printf("Vertices invalidos!\n");
        return;
    }

    No* novo = criarNo(v2);

    novo->prox = g->listaAdj[v1];
    g->listaAdj[v1] = novo;
}

// Imprimir grafo
void imprimirGrafo(Grafo* g) {
    printf("\nLista de adjacencia:\n");

    for (int i = 0; i < g->numVertices; i++) {
        printf("%d -> ", i);

        No* temp = g->listaAdj[i];

        while (temp != NULL) {
            printf("%d -> ", temp->numVertices);
            temp = temp->prox;
        }

        printf("NULL\n");
    }
}

// Liberar memória
void liberarGrafo(Grafo* g) {
    for (int i = 0; i < g->numVertices; i++) {
        No* temp = g->listaAdj[i];

        while (temp != NULL) {
            No* aux = temp;
            temp = temp->prox;
            free(aux);
        }
    }

    free(g);
}

int main() {
    int vertices, arestas;
    int v1, v2;

    printf("Numero de vertices: ");
    scanf("%d", &vertices);

    Grafo* g = criarGrafo(vertices);

    printf("Numero de arestas: ");
    scanf("%d", &arestas);

    for (int i = 0; i < arestas; i++) {
        printf("Aresta %d (origem destino): ", i + 1);
        scanf("%d %d", &v1, &v2);

        adicionarAresta(g, v1, v2);
    }

    imprimirGrafo(g);

    liberarGrafo(g);

    return 0;
}