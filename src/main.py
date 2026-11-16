from entendendo_algoritmos.dijkstra import dijkstra


def exe():
    costs, parents = dijkstra()

    print(costs)
    print(parents)


if __name__ == "__main__":
    exe()
