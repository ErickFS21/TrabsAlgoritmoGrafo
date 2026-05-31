#include <stdio.h>
#include <stdlib.h>

#define MAX 100

typedef struct No {
    int vertice;
    struct No* prox;
} No;

typedef struct {
    No* adj[MAX];
    int visitado[MAX];
    int numVertices;
} Grafo;

No* criarNo(int v) {
    No* novo = (No*) malloc(sizeof(No));

    if (novo == NULL) {
        printf("Erro de memoria\n");
        exit(1);
    }

    novo->vertice = v;
    novo->prox = NULL;

    return novo;
}

void inicializarGrafo(Grafo* g, int vertices) {
    g->numVertices = vertices;

    for (int i = 0; i < vertices; i++) {
        g->adj[i] = NULL;
        g->visitado[i] = 0;
    }
}

void adicionarAresta(Grafo* g, int origem, int destino) {
    No* novo = criarNo(destino);
    novo->prox = g->adj[origem];
    g->adj[origem] = novo;

    // grafo não direcionado
    novo = criarNo(origem);
    novo->prox = g->adj[destino];
    g->adj[destino] = novo;
}

void dfs(Grafo* g, int v) {
    printf("%d ", v);
    g->visitado[v] = 1;

    No* temp = g->adj[v];

    while (temp != NULL) {
        int adj = temp->vertice;

        if (!g->visitado[adj]) {
            dfs(g, adj);
        }

        temp = temp->prox;
    }
}

int main() {
    Grafo g;
    int vertices, arestas;
    int origem, destino, inicio;

    printf("Numero de vertices: ");
    scanf("%d", &vertices);

    inicializarGrafo(&g, vertices);

    printf("Numero de arestas: ");
    scanf("%d", &arestas);

    for (int i = 0; i < arestas; i++) {
        printf("Aresta %d (origem destino): ", i + 1);
        scanf("%d %d", &origem, &destino);

        if (origem >= vertices || destino >= vertices) {
            printf("Vertice invalido!\n");
            i--; // repete a leitura
            continue;
        }

        adicionarAresta(&g, origem, destino);
    }

    printf("Vertice inicial para DFS: ");
    scanf("%d", &inicio);

    if (inicio >= vertices) {
        printf("Vertice inicial invalido!\n");
        return 1;
    }

    printf("Resultado da DFS:\n");
    dfs(&g, inicio);

    printf("\n");

    return 0;
}