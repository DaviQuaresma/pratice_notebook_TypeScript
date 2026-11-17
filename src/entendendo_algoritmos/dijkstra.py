def found_on_lower_cost(costs, processed):
    print("Procurando o custo mais baixo")
    lower_cost = float("inf")
    lower_cost_vertice = None

    for vertice in costs:
        print(f"Vertice: {vertice}")
        cost = costs[vertice]
        print(f"Custo de acordo com vertice: {cost}")

        print(
            "Se o lower_cost for menos que o cost e o vertice não tiver sido processado, ele entra na condicão"
        )
        if cost < lower_cost and vertice not in processed:
            print("Entrou")
            print("Antigo lower_cost: ", lower_cost)
            lower_cost = cost
            print("Novo lower_cost: ", lower_cost)

            print("Antigo lower_cost_vertice: ", lower_cost_vertice)
            lower_cost_vertice = vertice
            print("Novo lower_cost_vertice: ", lower_cost_vertice)

    return lower_cost_vertice


def dijkstra():
    processed = []
    infinity = float("inf")

    graph = {}

    # Grafo
    graph["inicio"] = {}
    graph["inicio"]["A"] = 5
    graph["inicio"]["B"] = 2

    graph["A"] = {}
    graph["A"]["B"] = 10

    graph["B"] = {}
    graph["B"]["C"] = 20

    graph["C"] = {}
    graph["C"]["D"] = 1
    graph["C"]["fim"] = 30

    graph["D"] = {}
    graph["D"]["A"] = 1

    graph["fim"] = {}

    # Custos iniciais (apenas vizinhos diretos do "inicio" têm valores)
    costs = {}
    costs["A"] = 5
    costs["B"] = infinity
    costs["C"] = infinity
    costs["D"] = infinity
    costs["fim"] = infinity

    # Pais iniciais (apenas vizinhos diretos têm "inicio" como pai)
    parents = {}
    parents["A"] = "inicio"
    parents["B"] = None
    parents["C"] = None
    parents["D"] = None
    parents["fim"] = None

    # Algoritmo
    vertice = found_on_lower_cost(costs, processed)
    print("Retorna o vertice da função: ", vertice)

    while vertice is not None:
        print("Enquanto vertice is not None, ele roda")
        cost = costs[vertice]
        print("O custo atual de acordo com o vertice: ", cost)
        neighbors = graph[vertice]
        print("Os vizinhos atuais de acordo com o grafo[vertice]: ", neighbors)

        for n in neighbors:
            print("Iteração dentro dos vizinhos: ", n)
            new_cost = cost + neighbors[n]
            print("Novo new_cost que é igual a cost atual + neighbors[n]")

            print(
                "Se o costs[n] que é o cost da iteração for maior que o new_cost ele vai entrar na condição e atualizar os costs e parents"
            )
            if costs[n] > new_cost:
                print("Atualizando new_cost, antes: ", new_cost)
                costs[n] = new_cost
                print("Atualizando new_cost, depois: ", new_cost)
                print("Atualizando vertice, antes: ", vertice)
                parents[n] = vertice
                print("Atualizando vertice, depois: ", vertice)

        print("Appendando um vertice aos processados para ir ao outro vertice")
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
