
# Se quiser reconstruir o caminho
def reconstruct_path(parents, start, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()

    if path[0] != start:
        return None

    return path

def bellman_ford(vertices, edges, start):

    # distances: armazena o menor custo conhecido para cada vértice.
    # parents: armazena de qual vértice viemos para alcançar o destino com aquele custo.
    distances = {vertex: float("inf") for vertex in vertices}
    parents = {vertex: None for vertex in vertices}

    distances[start] = 0

    # Executa V - 1 passagens
    for _ in range(len(vertices) - 1):
        updated = False

        for u, v, weight in edges:
            if distances[u] == float("inf"):
                continue

            new_distance = distances[u] + weight

            if new_distance < distances[v]:
                distances[v] = new_distance
                parents[v] = u
                updated = True

        # Otimização: nenhuma distância mudou
        if not updated:
            break

    # Verifica a existência de ciclos negativos
    for u, v, weight in edges:
        if distances[u] != float("inf"):
            if distances[u] + weight < distances[v]:
                raise ValueError("Ciclo negativo detectado")

    return distances, parents


# (origem, destino, peso)
edges = [
    ("A", "B", 6),
    ("A", "C", 7),
    ("B", "C", 8),
    ("B", "D", 5),
    ("B", "E", -4),
    ("C", "D", -3),
    ("C", "E", 9),
    ("D", "B", -2),
    ("E", "A", 2),
    ("E", "D", 7),
]

vertices = ["A", "B", "C", "D", "E"]

distances, parents = bellman_ford(vertices, edges, "A")

print(distances)
print(parents)
