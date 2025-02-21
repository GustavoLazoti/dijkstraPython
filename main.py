import sys
# Olá, professor Gastón! Tudo bem? Aqui segue meu código do algoritmo, eu te indico onde pode alterar os valores para testalo com diferentes cenários! Obrigado!
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for _ in range(vertices)]

    def menor_distancia(self, distancias, visitados):
        menor_dist = sys.maxsize
        menor_indice = None

        # Procura pelo vértice com a menor distância mínima que ainda não foi visitado
        for v in range(self.vertices):
            if distancias[v] < menor_dist and not visitados[v]:
                menor_dist = distancias[v]
                menor_indice = v

        return menor_indice

    def dijkstra(self, inicio):
        distancias = [sys.maxsize] * self.vertices
        distancias[inicio] = 0
        visitados = [False] * self.vertices

        # Iteração para encontrar as distâncias mínimas para todos os vértices
        for _ in range(self.vertices):
            # Encontra o vértice com a menor distância mínima
            u = self.menor_distancia(distancias, visitados)
            visitados[u] = True

            # Atualiza as distâncias mínimas dos vértices adjacentes ao vértice atual
            for v in range(self.vertices):
                if self.grafo[u][v] > 0 and not visitados[v] and distancias[v] > distancias[u] + self.grafo[u][v]:
                    distancias[v] = distancias[u] + self.grafo[u][v]

        return distancias

# Exemplo de uso -----> Altere aqui para obter um problema e resposta diferente e correta!
g = Grafo(6)
g.grafo = [
    [0, 2, 4, 0, 0, 0],
    [2, 0, 1, 7, 0, 0],
    [4, 1, 0, 0, 3, 0],
    [0, 7, 0, 0, 1, 2],
    [0, 0, 3, 1, 0, 3],
    [0, 0, 0, 2, 3, 0]
]

vertice_inicial = 0
distancias = g.dijkstra(vertice_inicial)

print("Distâncias mínimas a partir do vértice inicial:")
for v in range(g.vertices):
    print(f"Vértice {v}: {distancias[v]}")
