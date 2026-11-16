
def found_on_lower_cost(costs, processed):
    lower_cost = float("inf")
    lower_cost_vertice = None

    for vertice in costs:
        cost = costs[vertice]

        if cost < lower_cost and vertice not in processed:
            lower_cost = cost
            lower_cost_vertice = vertice

    return lower_cost_vertice


def dijkstra():
    processed = []
    infinity = float("inf")

    graph = {}

    # Grafo
    graph["inicio"] = {}
    graph["inicio"]["A"] = 6
    graph["inicio"]["B"] = 2

    graph["A"] = {}
    graph["A"]["fim"] = 1

    graph["B"] = {}
    graph["B"]["A"] = 3
    graph["B"]["fim"] = 5

    graph["fim"] = {}

    # Custos
    costs = {}
    costs["A"] = 6
    costs["B"] = 2
    costs["fim"] = infinity

    # Pais
    parents = {}
    parents["A"] = "inicio"
    parents["B"] = "inicio"
    parents["fim"] = None

    # Algoritmo
    vertice = found_on_lower_cost(costs, processed)

    while vertice is not None:
        cost = costs[vertice]
        neighbors = graph[vertice]

        for n in neighbors:
            new_cost = cost + neighbors[n]

            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = vertice

        processed.append(vertice)

        vertice = found_on_lower_cost(costs, processed)

    return costs, parents

# Anotação sobre dificuldade no entendimento de atualização de parents:

# Na primeira iteração da menor escolha do grafo, ela vai passar no caminho até o fim e atualizar os parents, isso vai afetar a iterção do segundo vertice

# Primeiro vertice:
# I -> 2 -> A -> 1 -> B -> 3 -> F

# Ele começa no I e o custo para o vertice A é 2, após isso o caminho de A direto ao F custa mais caro que passar por B que custa 1, e depois disso o custo de B para F é 3.
# Atualiza o custo de B, antes I para B era custo 5, mas depois da atualização de A, o custo de I para B é de 3

# Segundo vertice:
# I -> 5 -> B (Esse seria o custo não atualizado para chegar a B, ou seja, 5)
# I -> 2 -> A -> 1 -> B (Esse é o custo atualizado para chegar a B ou seja, 3)